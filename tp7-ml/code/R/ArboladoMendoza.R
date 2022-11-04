library(readr)
library(ggplot2)
library(dplyr) # for data manipulation
library(caret) # for model-building
library(pROC) # for AUC calculations
source(".\\code\\R\\Operations.r")


#Import Dataset
arbolado_mza_dataset <- read_csv("data/PuntoB/arbolado-publico-mendoza-2021/arbolado-mza-dataset/arbolado-mza-dataset.csv")
arbolado_mza_dataset_test <- read_csv("data/PuntoB/arbolado-publico-mendoza-2021/arbolado-mza-dataset-test/arbolado-mza-dataset-test.csv")

#Modify Dataset

turnToNumeric<-function(dataset){
  for(i in seq(1,length(dataset))){
    if(class(pull(dataset,i))=="factor"){
      dataset[,i]<-as.numeric(pull(dataset,i))
    }
  }
  return(dataset)
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

modifyDataSet<-function(dataset){
  dataset$especie<-factor(dataset$especie)
  dataset$altura<-factor(dataset$altura)
  dataset$diametro_tronco<-factor(dataset$diametro_tronco)
  dataset$seccion<-factor(dataset$seccion)
  dataset$cric_tronco_cm_cat<-factor(addCircCat(dataset))
  dataset<-dataset[,-c(3,10,11)]
  return(dataset)
}

arbolado_mza_dataset <- modifyDataSet(arbolado_mza_dataset)
arbolado_mza_dataset_numeric <- addFeatures(arbolado_mza_dataset[seq(1,600),])
write.csv(arbolado_mza_dataset_numeric,".//data//PuntoB//arbolado-mza-dataset-featured.csv")
arbolado_mza_dataset_numeric <- addFeatures(arbolado_mza_dataset_test)

arbolado_mza_dataset<-arbolado_mza_dataset_numeric
arbolado_mza_dataset<-arbolado_mza_dataset %>% mutate(inclinacion_peligrosa=ifelse(inclinacion_peligrosa=='1','si','no'))
arbolado_mza_dataset$inclinacion_peligrosa <-as.factor(arbolado_mza_dataset$inclinacion_peligrosa)

#validation con casos positivos
flag<-TRUE
while(flag){
  Idx<- createDataPartition(arbolado_mza_dataset$id,p=0.8,list=FALSE,times=1)
  trainingSet <- arbolado_mza_dataset[Idx,]
  validationSet <- arbolado_mza_dataset[-Idx,]
  if(length(unique(validationSet$inclinacion_peligrosa))>=2){
    flag<-FALSE
  }
}

#Dataset analysis
freq(trainingSet,plot = FALSE)

#Folds
ctrl <- trainControl(
                    method = "repeatedcv",
                     number = 3,
                     repeats = 0,
                     classProbs = TRUE,
                     verboseIter = TRUE,
                     p = 0.90,
                     sampling = "up"
                     )

#fold seed
set.seed(1111)

#training
form<-formula(inclinacion_peligrosa ~.)

#wight not working(best 0.6 without tune)
createWeightModel<-function(data,weightDiff){
  Ntotal <- nrow(trainingSet[trainingSet$inclinacion_peligrosa == "no",])
  Ptotal <- nrow(trainingSet[trainingSet$inclinacion_peligrosa == "si",])
  Pcw <- (weightDiff + 1)/2
  Ncw <- (1-Pcw) 
  m<-ifelse(data$inclinacion_peligrosa == "si", trunc(10*Pcw) ,trunc(10*Ncw))
  return(m)  
}

tune <- expand.grid(.mincriterion = 0.70, 
                    .maxdepth = as.numeric(seq(3,10,1)))
model_tree<-train(form,
                    data = trainingSet,
                  #weights = createWeightModel(trainingSet,0.6),
                    tuneGrid = tune,
                    method = "ctree2",
                    metric = "ROC",
                    trControl = ctrl)
  
#Validation
preds=predict(model_tree,validationSet,type='prob')
if(unique(validationSet$inclinacion_peligrosa)[1] == "no"){
  validationSet$inclinacion_peligrosa <- ifelse(validationSet$inclinacion_peligrosa == "si",1,0)
}
preds <- ifelse(preds$si >= 0.5,1,0)
print(getConfusionMatrix(validationSet$inclinacion_peligrosa,preds))

#Submission
testSet<- modifyDataSet(arbolado_mza_dataset_test)
preds=predict(model_tree,testSet,type='raw')
preds<- ifelse(preds == "si",1,0)
submission<-data.frame(id=testSet$id,inclinacion_peligrosa=preds)
write_csv(submission,"./data/PuntoB/Envios/arbolado-mza-dataset-envio-9.csv")
