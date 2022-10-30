#Libraries
library(dplyr)
library(funModeling)
library(ggplot2)
library(ggbeeswarm)
library(cowplot)
library(rpart)

#A
#1
#Load CSV
dataSet <-read.csv("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\arbolado-mza-dataset.csv")
#samples
size<-nrow(dataSet)
index<-sample(seq(1:size),trunc(size*0.8))
training <- dataSet[index,]
testing <- dataSet[-index,]
#Save CSV
write.csv(testing,"C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\arbolado-publico-mendoza-2021-validation.csv")
write.csv(training,"C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\arbolado-publico-mendoza-2021-train.csv")

#2
#training dataset analysis
#Pregunta 1
freq(training$inclinacion_peligrosa,na.rm=TRUE,plot=TRUE)
#se trata de una distribucion binomial donde n=31912 y p=0.1128
#Pero se puede aproximar a una normal si np>=5 y n(1-p)>=5
# np=2880 y n(1-p)=22648 Por lo que se puede aporximar con una distribucion normal

#Pregunta 2
freq(training$nombre_seccion,plot=TRUE)
#La mayor cantidad de arboles está en Residencial Norte
freq(subset(training[c("nombre_seccion","inclinacion_peligrosa")],training$inclinacion_peligrosa == 1),plot=TRUE)
# la mayor cantidad de arboles peligrosos se encuentran en Residencial Sur
#Como la cantidad de arboles por seccion son distinta no podemos suponer que
#una zona es más peligrosa que otra debido a que si tiene más arboles probablemente sea mas peligrosa

#Pregunta 3
freq(training$especie,plot=TRUE)
#la mayor cantidad de arboles son de especie Morena
freq(subset(training[c("especie","inclinacion_peligrosa")],training$inclinacion_peligrosa == 1),plot=TRUE)
# la especie con mayor cantidad de arboles peligrosos es la especie Morera

#no podemos asumir que una especie es más peligrosa que otra debido a que no hay una cantidad pareja de especies
#como el 41.26% de especies son Morena entonces es evidente que sera la más peligrosa.

training %>%
  count(especie,nombre_seccion) %>%
  ggplot(aes(x=nombre_seccion,y=especie)) + 
  geom_tile(aes(fill=n),colour="black") +
  scale_fill_gradient(low = "grey", high = "red2") +
  labs(x="Especies",y="Seccion",fill="Cantidad") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

#3
#3.2
plot1 <- ggplot(data=training,aes(x=circ_tronco_cm)) + geom_histogram(aes(x=circ_tronco_cm),bins=40)
plot2 <- ggplot(data=training,aes(x=circ_tronco_cm)) + geom_histogram(aes(x=circ_tronco_cm),bins=80)
plot3 <- ggplot(data=training,aes(x=circ_tronco_cm)) + geom_histogram(aes(x=circ_tronco_cm),bins=100)
plot4 <- ggplot(data=training,aes(x=circ_tronco_cm)) + geom_histogram(aes(x=circ_tronco_cm),bins=120)


plot_grid(plot1, plot2, plot3 ,plot4, 
          labels = c("40 bins", "80 bins","100 bins", "120 bins"),
          label_size = 10,
          label_x =0.7,
          label_y = 0.7,
          ncol = 2, nrow = 2)
#3.3
plot1 <- ggplot(data=training,aes(x=circ_tronco_cm,fill=factor(inclinacion_peligrosa))) + geom_histogram(aes(x=circ_tronco_cm),position="stack",bins=40) + scale_fill_discrete("Peligro",labels=c("no","si"))
plot2 <- ggplot(data=training,aes(x=circ_tronco_cm,fill=factor(inclinacion_peligrosa))) + geom_histogram(aes(x=circ_tronco_cm),position="stack",bins=80) + scale_fill_discrete("Peligro",labels=c("no","si"))
plot3 <- ggplot(data=training,aes(x=circ_tronco_cm,fill=factor(inclinacion_peligrosa))) + geom_histogram(aes(x=circ_tronco_cm),position="stack",bins=100) + scale_fill_discrete("Peligro",labels=c("no","si"))
plot4 <- ggplot(data=training,aes(x=circ_tronco_cm,fill=factor(inclinacion_peligrosa))) + geom_histogram(aes(x=circ_tronco_cm),position="stack",bins=120) + scale_fill_discrete("Peligro",labels=c("no","si"))


plot_grid(plot1, plot2, plot3 ,plot4, 
          labels = c("40 bins", "80 bins","100 bins", "120 bins"),
          label_size = 10,
          label_x =0.4,
          label_y = 0.7,
          ncol = 2, nrow = 2)
#3.4
getn <- function(val){
  n <- ifelse(val > 300 ,1,
              ifelse(val> 200 ,2,
                     ifelse(val> 100,3,4)
                     )
              )
}

addCircCat<-function(dataset){
  cat_vector <- vector("character",length = 0)
  for(i in seq(1,nrow(dataset))){
    cat_vector <- c(cat_vector,switch(getn(dataset[i,"circ_tronco_cm"]) ,"muy alto","alto","medio","bajo"))
  }
  dataset$circ_tronco_cm_cat <- cat_vector
  return(dataset)
}
training<-addCircCat(training)
write.csv(training,"C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\arbolado-publico-mendoza-2021-circ_tronco_cm-train.csv")
#4.a
predictProb<-function(dataframe){
  size<-nrow(dataframe)
  dataframe$prediction_prob<-sample(c(0,1),size,replace=TRUE)
  return(dataframe)
}
#4.b
random_classifier<-function(dataframe){
  dataframe<-predictProb(dataframe)
  vector<-vector(length = 0)
  for(i in seq(1,nrow(dataframe))){
    vector <- c(vector,ifelse(dataframe[i,"prediction_prob"] > 0.5,1,0))
  }
  dataframe$prediction_class<-vector
  return(dataframe)
}
#4.c
validation <- read.csv("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\arbolado-publico-mendoza-2021-validation.csv")
validation <- random_classifier(validation)
#4.d
sensitivity<-function(TP,FN) round(TP/(TP+FN),3)
specificity<-function(TN,FP) round(TN/(TN+FP),3)
negativePredictive<-function(TN,FN) round(TN/(TN+FN),3)
precision<-function(TP,FP) round(TP/(TP+FP),3)

getConfusionMatrix<-function(actual_class,predicted_class){
  n<-length(actual_class)
  predicted<-actual_class[actual_class == predicted_class]
  notpredicted<-actual_class[!(actual_class == predicted_class)]
  TP <-length(predicted[predicted == 1])
  TN <-length(predicted[predicted == 0])
  FP <-length(notpredicted[notpredicted == 1])
  FN <-length(notpredicted[notpredicted == 0])
  f1 <-c(n,"Predicted Positive","Predicted Negative","total")
  f2 <-c("Actual Positive",TP,FN,sensitivity(TP,FN))
  f3 <-c("Actual Negative",FP,TN,specificity(FP,TN))
  f4 <-c("total",precision(TP,FP),negativePredictive(FN,TN),"")
  cofusionMatrix <- rbind(f1,f2,f3,f4)
  return(cofusionMatrix)
}
print(getConfusionMatrix(validation$inclinacion_peligrosa,validation$prediction_class))
#5
biggerclass_classifier<-function(dataframe){
  fdata<-freq(dataframe$inclinacion_peligrosa)
  value <- fdata[fdata$frequency == max(fdata$frequency),"var"]
  dataframe$prediction_class<-value
  return(dataframe)
}
#6
validation <- read.csv("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\arbolado-publico-mendoza-2021-validation.csv")
validation <- biggerclass_classifier(validation)
print(getConfusionMatrix(validation$inclinacion_peligrosa,validation$prediction_class))
#7
create_folds<-function(dataset,amount){
  folds<-list()
  size<-trunc(nrow(dataset)/amount)
  j<-1
  for(i in seq(1,amount)){
    idx <- sample(rownames(dataset),size)
    folds <- append(folds,list(as.numeric(idx)))
    j<-j+1
  }
  return(folds)
}

promConfus<-function(listofConfus,folds){
  TP<-0
  TN<-0
  FP<-0
  FN<-0
  for(i in seq(1,folds)){
    TP <- as.numeric(listofConfus[[i]][2,2]) + TP
    TN <- as.numeric(listofConfus[[i]][3,3]) + TN
    FP <- as.numeric(listofConfus[[i]][3,2]) + FP
    FN <- as.numeric(listofConfus[[i]][2,3]) + FN
  }
  TP<-TP/folds
  TN<-TN/folds
  FP<-FP/folds
  FN<-FN/folds
  f1 <-c( as.numeric(listofConfus[[1]][1,1]),"Predicted Positive","Predicted Negative","total")
  f2 <-c("Actual Positive",TP,FN,sensitivity(TP,FN))
  f3 <-c("Actual Negative",FP,TN,specificity(FP,TN))
  f4 <-c("total",precision(TP,FP),negativePredictive(FN,TN),"")
  matrix<-rbind(f1,f2,f3,f4)
  return(matrix)
}

cross_validation<-function(dataframe,foldsNum){
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
    
    trainSet$inclinacion_peligrosa<-factor(trainSet$inclinacion_peligrosa)
    trainSet$altura<-factor(trainSet$altura)
    trainSet$circ_tronco_cm_cat<-factor(trainSet$circ_tronco_cm_cat)
    
    tree_model <- rpart(inclinacion_peligrosa ~especie+altura+circ_tronco_cm_cat+diametro_tronco+long+lat+seccion+area_seccion,data=trainSet)
    
    print(rpart.plot::rpart.plot(tree_model))
    
    predicted_class<-predict(tree_model,testSet,type="class")
    resultMatrix[[i]]<-getConfusionMatrix(testSet$inclinacion_peligrosa,predicted_class)
  }
  matrix<-promConfus(resultMatrix,foldsNum)
  return(matrix)
}
validation <- read.csv("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\arbolado-publico-mendoza-2021-validation.csv")
validation<-addCircCat(validation)
print(cross_validation(validation,2))

tree_model <- rpart(inclinacion_peligrosa ~especie+altura+circ_tronco_cm_cat+diametro_tronco+long+lat+seccion+area_seccion,data=validation)

rpart.plot::rpart.plot(tree_model)
