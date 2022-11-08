import pandas as pd
from Agent import Agent

if __name__== "__main__":
    path = ".\\data\\PuntoC\\tennis.csv"
    dataset = pd.read_csv(path)
    outputLabel = dataset.columns[len(dataset.columns)-1]
    ag = Agent(outputLabel)
    #divide
    trainSet = dataset.sample(frac=0.8,random_state=1)
    print(trainSet)
    testSet = dataset.drop(trainSet.index)
    testSet.columns = testSet.columns.str.replace(str(outputLabel),str(outputLabel) + "_orig")
    treeModel = ag.decisionTreeLearning(trainSet)
    treeModel.show()
    ag.test(testSet,treeModel)
    print(testSet)
    
