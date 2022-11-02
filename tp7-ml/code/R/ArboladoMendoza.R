library(readr)
library(dplyr)
library(ggplot2)
library(imbalance)
source(".\\code\\R\\Operations.r")

#Import Dataset
arbolado_mza_dataset <- read_csv("data/PuntoB/arbolado-publico-mendoza-2021/arbolado-mza-dataset/arbolado-mza-dataset.csv")
arbolado_mza_dataset_test <- read_csv("data/PuntoB/arbolado-publico-mendoza-2021/arbolado-mza-dataset-test/arbolado-mza-dataset-test.csv")

#Modify Dataset
testSet<- modifyDataSet(arbolado_mza_dataset_test)

trainingSet<- modifyDataSet(arbolado_mza_dataset)
trainingSet$inclinacion_peligrosa <- factor(trainingSet$inclinacion_peligrosa)

#Dataset analysis
freq(trainingSet,plot = TRUE)

#circ_tronco_cm se puede clasificar con el diametro_tronco
#cor(trainingSet$circ_tronco_cm,as.numeric(trainingSet$diametro_tronco),method="pearson")
#ggplot(trainingSet, aes(x = diametro_tronco,y=circ_tronco_cm,colour=diametro_tronco))+geom_count()

#CrossValidation
form<-formula(inclinacion_peligrosa ~especie+altura+diametro_tronco+seccion+long+lat)
cross_validation(trainingSet,form,foldsNum=3,
                 c(cp = 0.000001, minsplit=100, minbucket=2, maxdepth=15)
                 )

#Balance Dataset
oversampled<-as.numeric(as.data.frame(trainingSet))
imbalanceRatio(oversampled, classAttr = "inclinacion_peligrosa")
overSampledSet<-oversample(oversampled,ratio=0.3, classAttr = "inclinacion_peligrosa")

#Evaluation
tree_model<-rpart(formula=form,data=trainingSet,cp = 0.000001, minsplit=7, minbucket=6, maxdepth=7)
rpart.plot(tree_model)

preds_tree=predict(tree_model,testSet,type='class')
submission<-data.frame(id=testSet$id,inclinacion_peligrosa=preds_tree)
write_csv(submission,"./arbolado-mza-dataset-envio-3.csv")
