# Cross Validation TP7 #

## Código ##

```R
create_folds<-function(dataset,amount){
  folds<-list()
  size<-trunc(nrow(dataset)/amount)
  for(i in seq(1,amount)){
    idx <- sample(rownames(dataset),size)
    folds <- append(folds,list(idx))
  }
  return(folds)
}
```

```R
cross_validation<-function(dataframe,foldsNum){
  folds<-create_folds(dataframe,foldsNum) 
  resultMatrix<-list()
  for(i in seq(1,foldsNum)){
    #indices
    testIdx <- folds[[i]]
    trainFolds <- folds[-i]
    trainIdx <- c()
    for(j in seq(1,length(trainFolds))){
      trainIdx <- append(trainIdx,trainFolds[[j]])
    }
    #Sets
    trainSet<-dataframe[trainIdx,]
    testSet<-dataframe[testIdx,]
    #Model
    tree_model<-rpart(inclinacion_peligrosa ~especie+altura+circ_tronco_cm_cat+seccion+diametro_tronco,data=trainSet,
                      minbucket=2,minsplit=3,maxdepth=6,cp=0.00001)
    rpart.plot::rpart.plot(tree_model)
    #Result table
    predicted_class<-predict(tree_model,testSet,type="class")
    resultMatrix[[i]]<-getConfusionMatrix(testSet$inclinacion_peligrosa,predicted_class)
  }
  matrix<-promConfus(resultMatrix,foldsNum)
  return(matrix)
}
```

## Resultados ##

### Matriz de confusion ###

|     25527     |Predicted Positive|Predicted Negative|total|
|:-------------:|:----------------:|:----------------:|:---:|
|Actual Positive|       5.667      |         3        |0.654|
|Actual Negative|       969.667    |     7530.667     |0.114| 
|     total     |       0.006      |         0        |0.886|

### Desviación Estándar ###

|D.E|values|
|:-:|:----:|
| TP|1.155 |
| FP|13.868|
| TN|13.051|
| FN|0     |
