#Libraries
library(dplyr)
library(funModeling)
library(ggplot2)
library(ggbeeswarm)
library(cowplot)
library(rpart)
library(rpart.plot)

addRarezaAltura<-function(dataset){
  l <- list()
  for(i in unique(dataset$especie)){
    especieSet<-dataset[dataset$especie==i,"altura"]
    categories <- freq(especieSet)[,1]
    rarity <-switch(length(categories),c("normal"),c("común","raro"),c("común","normal","raro"),c("muy común","normal","raro","muy raro"))
    l[i] <- list(rbind(categories,rarity))
  }
  arr <- c()
  for(j in seq(1,length(l[dataset$especie]))){
    freqMat<-l[as.character(dataset$especie)][[j]]
    altura<-dataset[[j,"altura"]]
    alturaIdx<-which(freqMat[1,] == as.character(altura))
    if(length(alturaIdx) < 1){
      print(j)
    }
    arr <- rbind(arr,freqMat[2,alturaIdx])
  }
  return(arr)
}

addEsbeltez <- function(dataset){
  numAltura <- as.numeric(dataset$altura)
  arr<- numAltura*dataset$cric_diamtero_cm
  return(arr)
}

addCircCat<-function(dataset){
  col<-pull(dataset,"circ_tronco_cm")
  arr <- ifelse(col > 300 ,"muy alto",ifelse(col > 200 ,"alto",ifelse(col > 100,"medio","bajo")))
  return(arr)
}

addDiametro<-function(dataset){
  arr <- 3.14*pull(dataset,"circ_tronco_cm")
  return(arr)
}


predictProb<-function(dataframe){
  size<-nrow(dataframe)
  dataframe$prediction_prob<-sample(c(0,1),size,replace=TRUE)
  return(dataframe)
}

random_classifier<-function(dataframe){
  dataframe<-predictProb(dataframe)
  vector<-vector(length = 0)
  for(i in seq(1,nrow(dataframe))){
    vector <- c(vector,ifelse(dataframe[i,"prediction_prob"] > 0.5,1,0))
  }
  dataframe$prediction_class<-vector
  return(dataframe)
}

sensitivity<-function(TP,FN) round(TP/(TP+FN),3)
specificity<-function(TN,FP) round(TN/(TN+FP),3)
negativePredictive<-function(TN,FN) round(TN/(TN+FN),3)
precision<-function(TP,FP) round(TP/(TP+FP),3)
accuracy<-function(TP,TN,FP,FN) round((TP+TN)/(TP+TN+FP+FN),3)

getConfusionMatrix<-function(actual_class,predicted_class){
  n<-length(actual_class)
  predicted<-predicted_class[actual_class == predicted_class]
  notpredicted<-predicted_class[!(actual_class == predicted_class)]
  TP <-length(predicted[predicted == 1])
  TN <-length(predicted[predicted == 0])
  FP <-length(notpredicted[notpredicted == 1])
  FN <-length(notpredicted[notpredicted == 0])
  f1 <-c(n,"Predicted Positive","Predicted Negative","total")
  f2 <-c("Actual Positive",TP,FN,sensitivity(TP,FN))
  f3 <-c("Actual Negative",FP,TN,specificity(FP,TN))
  f4 <-c("total",precision(TP,FP),negativePredictive(FN,TN),accuracy(TP,TN,FP,FN))
  cofusionMatrix <- rbind(f1,f2,f3,f4)
  return(cofusionMatrix)
}

biggerclass_classifier<-function(dataframe){
  fdata<-freq(dataframe$inclinacion_peligrosa)
  value <- fdata[fdata$frequency == max(fdata$frequency),"var"]
  dataframe$prediction_class<-value
  return(dataframe)
}

create_folds<-function(dataset,amount){
  folds<-list()
  size<-trunc(nrow(dataset)/amount)
  for(i in seq(1,amount)){
    idx <- sample(rownames(dataset),size)
    folds <- append(folds,list(idx))
  }
  return(folds)
}

promConfus<-function(listofConfus,folds){
  TPV<-c()
  TNV<-c()
  FPV<-c()
  FNV<-c()
  n<-0
  for(i in seq(1,folds)){
    n <- as.numeric(listofConfus[[i]][1,1]) + n
    TPV <- c(TPV,as.numeric(listofConfus[[i]][2,2]))
    TNV <- c(TNV,as.numeric(listofConfus[[i]][3,3]))
    FPV <- c(FPV,as.numeric(listofConfus[[i]][3,2]))
    FNV <- c(FNV,as.numeric(listofConfus[[i]][2,3]))
  }
  TP<-round(sum(TPV)/folds,3)
  TN<-round(sum(TNV)/folds,3)
  FP<-round(sum(FPV)/folds,3)
  FN<-round(sum(FNV)/folds,3)
  f1 <-c(n,"Predicted Positive","Predicted Negative","total",paste("D.E de TP:",as.character(round(sd(TPV),3))))
  f2 <-c("Actual Positive",TP,FN,sensitivity(TP,FN),paste("D.E de FP:",as.character(round(sd(FPV),3))))
  f3 <-c("Actual Negative",FP,TN,specificity(FP,TN),paste("D.E de TN:",as.character(round(sd(TNV),3))))
  f4 <-c("total",precision(TP,FP),negativePredictive(FN,TN),accuracy(TP,TN,FP,FN),paste("D.E de FN:",as.character(round(sd(FNV),3))))
  matrix<-rbind(f1,f2,f3,f4)
  return(matrix)
}

#realiza una cross validation del dataframe enviado
cross_validation<-function(dataframe,formula,foldsNum,settings){
  folds<-create_folds(dataframe,foldsNum) 
  resultMatrix<-list()
  for(i in seq(1,foldsNum)){
    testIdx <- folds[[i]]
    trainFolds <- folds[-i]
    trainIdx <- c()
    for(j in seq(1,length(trainFolds))){
      trainIdx <- append(trainIdx,trainFolds[[j]])
    }
    
    trainSet<-dataframe[trainIdx,]
    testSet<-dataframe[testIdx,]
    
    tree_model<-rpart(formula=formula, data=trainSet,
                      cp = settings[1],minsplit = settings[2],
                      minbucket=settings[3], maxdepth = settings[4])
    #summary(tree_model)
    print(tree_model)
    #rpart.plot(tree_model)
    predicted_class<-predict(tree_model,testSet,type="class")
    resultMatrix[[i]]<-getConfusionMatrix(testSet[[length(testSet)]],predicted_class)
  }
  matrix<-promConfus(resultMatrix,foldsNum)
  return(matrix)
}

setRate<-function(row,dataset){
  if(length(row)==length(dataset)){
    attsRate <-c() 
    for(att in seq(2,length(dataset))){
      sum <- 0
      if(names(dataset)[att]!="inclinacion_peligrosa"){
        for(r in seq(1,nrow(dataset))){
          sum <- sum + abs(row[att] - dataset[r,att])
        }
        attsRate<-rbind(attsRate,c(sum/nrow(dataset))[[1]])
      }
    }  
  }
  attsRate<-rbind(attsRate,sum(attsRate))
  return(attsRate)
}

addFeatures<-function(dataset){
  arboles<-turnToNumeric(dataset)
  orig_size<-length(arboles)
  new_att <- orig_size-1
  new_columns<-seq(orig_size+1, orig_size + new_att )
  old_columns<-seq(1,orig_size)
  
  arboles[,new_columns] <- NaN
  names(arboles)[length(arboles)]<-"puntaje"
  arboles[arboles$inclinacion_peligrosa == 1,new_columns] <- 0
  arboles_peligrosos <- arboles[arboles$inclinacion_peligrosa == 1,old_columns]
  for(row in seq(1,nrow(arboles))){
    print(row)
    arbol<-arboles[row,old_columns]
    if(arbol$inclinacion_peligrosa == 0){
      rates <- setRate(arbol,arboles_peligrosos)
      arboles[row,new_columns]<-as.list(rates)  
    }
  }
  return(arboles)
}
