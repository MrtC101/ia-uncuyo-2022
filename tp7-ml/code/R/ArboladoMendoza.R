library(readr)
library(ggplot2)
library(dplyr) # for data manipulation
library(caret) # for model-building
library(pROC) # for AUC calculations
source(".\\code\\R\\Operations.R")




turnToNumeric<-function(dataset){
  for(i in seq(1,length(dataset))){
    if(class(pull(dataset,i))=="factor"){
      dataset[,i]<-as.numeric(pull(dataset,i))
    }
  }
  return(dataset)
}


preProcess<-function(dataset){
  dataset$cric_tronco_cm_cat<-factor(addCircCat(dataset))
  dataset$cric_diamtero_cm<-addDiametro(dataset)
  dataset$esbeltez<-addEsbeltez(dataset)
  dataset$rareza_de_altura<-factor(addRarezaAltura(dataset))
  return(dataset)
}

toFractor<-function(dataset){
  dataset$especie<-factor(dataset$especie)
  dataset$altura<-factor(dataset$altura)
  dataset$diametro_tronco<-factor(dataset$diametro_tronco)
  dataset$seccion<-factor(dataset$seccion)
  return(dataset)
}

#Import Dataset
arbolado_mza_dataset <- read_csv("data/PuntoB/arbolado-publico-mendoza-2021/arbolado-mza-dataset/arbolado-mza-dataset.csv")

#Modify Dataset
arbolado_mza_dataset<-arbolado_mza_dataset[,-c(3)]
arbolado_mza_dataset <- toFractor(arbolado_mza_dataset)
arbolado_mza_dataset <- preProcess(arbolado_mza_dataset)
write.csv(arbolado_mza_dataset,".//data//PuntoB//arbolado-mza-dataset-featured.csv",row.names = FALSE)

arbolado_mza_dataset<-read_csv(".//data//PuntoB//arbolado-mza-dataset-featured.csv")
arbolado_mza_dataset <- toFractor(arbolado_mza_dataset)
arbolado_mza_dataset$rareza_de_altura<-factor(arbolado_mza_dataset$rareza_de_altura)

#arbolado_mza_dataset<-turnToNumeric(arbolado_mza_dataset)
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
                     #repeats = 1,
                     classProbs = TRUE,
                     verboseIter = TRUE,
                     p = 0.90,
                     sampling = "smote"
                     )

#fold seed
set.seed(3333)

#training
form<-formula(inclinacion_peligrosa ~ especie + circ_tronco_cm + diametro_tronco + long + lat + seccion + esbeltez + rareza_de_altura)

#wight not working(best 0.6 without tune)
createWeightModel<-function(data,weightDiff){
  Ntotal <- nrow(trainingSet[trainingSet$inclinacion_peligrosa == "no",])
  Ptotal <- nrow(trainingSet[trainingSet$inclinacion_peligrosa == "si",])
  Pcw <- (weightDiff + 1)/2
  Ncw <- (1-Pcw) 
  m<-ifelse(data$inclinacion_peligrosa == "si", trunc(10*Pcw) ,trunc(10*Ncw))
  return(m)  
}

tune <- expand.grid(.mincriterion = as.numeric(0.5), 
                    .maxdepth = as.numeric(10)
)

#weights = createWeightModel(trainingSet,0.6),

model_tree<-train(form,data = trainingSet,
                    tuneGrid = tune,
                    method = "ctree2",
                    metric = "ROC",
                    trControl = ctrl)
plot(model_tree$finalModel)
#Validation
preds=predict(model_tree,validationSet,type='raw')
if(unique(validationSet$inclinacion_peligrosa)[1] == "no" | unique(validationSet$inclinacion_peligrosa)[1] == "si"){
  validationSet$inclinacion_peligrosa <- ifelse(validationSet$inclinacion_peligrosa == "si",1,0)
}
if(unique(preds)[1] == "no" | unique(preds)[1] == "si"){
  preds <- ifelse(preds == "si",1,0)
}else{
  preds <- ifelse(preds$si >= 0.5,1,0)
}
print(getConfusionMatrix(validationSet$inclinacion_peligrosa,preds))

#Submission
arbolado_mza_dataset_test <- read_csv("data/PuntoB/arbolado-publico-mendoza-2021/arbolado-mza-dataset-test/arbolado-mza-dataset-test.csv")

testSet <- toFractor(arbolado_mza_dataset_test)
testSet <- preProcess(testSet)
#testSet <- turnToNumeric(testSet)

preds=predict(model_tree,testSet,type='raw')
preds<- ifelse(preds == "si",1,0)
submission<-data.frame(id=testSet$id,inclinacion_peligrosa=preds)
write_csv(submission,"./data/PuntoB/Envios/arbolado-mza-dataset-envio-15.csv")
