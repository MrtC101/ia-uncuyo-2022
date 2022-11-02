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
```

## Resultados ##

### Matriz de confusion ###

|     31911     |Predicted Positive|Predicted Negative|total|
|:-------------:|:----------------:|:----------------:|:---:|
|Actual Positive|       146.333      |        1040        |0.123|
|Actual Negative|       161    |     9289.667     |0.017| 
|     total     |       0.476      |       0.101        |0.887|

### Desviación Estándar ###

|D.E|values|
|:-:|:----:|
| TP|19.858|
| FP|10.536|
| TN|37.166|
| FN|12.166|
