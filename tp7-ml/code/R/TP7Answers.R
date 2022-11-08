#Libraries
library(readr)
library(dplyr)
library(funModeling)
library(ggplot2)
library(ggbeeswarm)
library(cowplot)
library(rpart)
source(".\\code\\R\\Operations.r")

#A
#1
#Load CSV
dataSet <-read.csv("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\PuntoA\\arbolado-mza-dataset.csv")
#samples
size<-nrow(dataSet)
index<-sample(seq(1:size),trunc(size*0.8))
training <- dataSet[index,]
testing <- dataSet[-index,]
#Save CSV
write.csv(testing,"C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\PuntoA\\arbolado-publico-mendoza-2021-validation.csv")
write.csv(training,"C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\PuntoA\\arbolado-publico-mendoza-2021-train.csv")

#2
#training dataset analysis
#Pregunta 1
freq(training$inclinacion_peligrosa,na.rm=TRUE,plot=TRUE)

#Pregunta 2
freq(training$nombre_seccion,plot=TRUE)
freq(subset(training[c("nombre_seccion","inclinacion_peligrosa")],training$inclinacion_peligrosa == 1),plot=TRUE)

#Pregunta 3
freq(training$especie,plot=TRUE)
freq(subset(training[c("especie","inclinacion_peligrosa")],training$inclinacion_peligrosa == 1),plot=TRUE)

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
training<-addCircCat(training)
write.csv(training,"C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\PuntoA\\arbolado-publico-mendoza-2021-circ_tronco_cm-train.csv")
#4.c
validation <- read.csv("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\PuntoA\\arbolado-publico-mendoza-2021-validation.csv")
validation <- random_classifier(validation)
#4.d
print(getConfusionMatrix(validation$inclinacion_peligrosa,validation$prediction_class))
#5
#6
validation <- read.csv("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\tp7-ml\\data\\PuntoA\\arbolado-publico-mendoza-2021-validation.csv")
validation <- biggerclass_classifier(validation)
print(getConfusionMatrix(validation$inclinacion_peligrosa,validation$prediction_class))
#7
arbolado_mza_dataset <- read_csv("data/PuntoB/arbolado-publico-mendoza-2021/arbolado-mza-dataset/arbolado-mza-dataset.csv")

trainingSet<- modifyDataSet(arbolado_mza_dataset)
trainingSet$inclinacion_peligrosa <- factor(trainingSet$inclinacion_peligrosa)
print(cross_validation(trainingSet,formula(inclinacion_peligrosa ~especie+altura+diametro_tronco+seccion+long+lat),3,
                       c(cp = 0.000001, minsplit=100, minbucket=2, maxdepth=15)
))

