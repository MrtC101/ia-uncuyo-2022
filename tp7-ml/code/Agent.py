from lib2to3.pytree import Node
from operator import index
from unittest import result
from pandas.core.arrays import ExtensionArray
from array import array
import random
import math
import pandas as pd
import numpy as np
import treelib as t

class Agent:
    
    outputAtt = 'Null'
    
    #constructor
    def __init__(self,outputAttribute):
        self.outputAtt = outputAttribute 

    # Retorna un árbol con la entrada en el nodo raíz. 
    def newTree(self,attribute) -> t.Tree:
        tree = t.Tree()
        root = t.Node(tag=str(attribute),identifier=str(attribute),data=attribute)
        tree.add_node(root)
        return tree

    # Retorna los valores únicos que se presentan en una columna del dataframe
    def valuesOfColumn(self,dataset : pd.DataFrame, name : str) -> (np.ndarray | ExtensionArray):
        return pd.unique(dataset[name])

    #Retorna el único valor que hay en la columna de salida del dataframe
    def getUniqueOutput(self, dataset : pd.DataFrame) -> t.Node:
        output = self.valuesOfColumn(dataset,self.outputAtt)
        return t.Node(tag=None,identifier=None,data=output[0])

    #Cuenta la cantidad de valores de salida distintos que se presentan en la columna se salida del dataframe
    def countOutputValues(self,dataset : pd.DataFrame):
        serieOfValues = dataset.nunique('index')
        number = serieOfValues.get(self.outputAtt)
        return number
    
    # Devuelve el valor de salida más común entre los ejemplos de entrada
    def plularityValue(self, dataset : pd.DataFrame) -> t.Node:   
        outputs = dataset[str(self.outputAtt)] #?
        outputValues = pd.unique(dataset[str(self.outputAtt)]);
        mostCommon = (outputValues[0],0)
        for value in outputValues:
            currentNum = 0
            for i in range(0,outputs.size):
                if value == outputs[i]: #?
                    currentNum += 1
            if mostCommon[1] < currentNum or ( mostCommon[1] == currentNum and random.choice([True,False]) ):
                mostCommon = (value, currentNum)
        return t.Node(tag=None,identifier=None,data=mostCommon[0])
    
    def filterDataframe(self, dataset : pd.DataFrame, attribute, value) -> pd.DataFrame:
        res = dataset[dataset[attribute] == value]
        return res 

    #Cuenta la cantidad de filas del ejemplo que no son clasificables
    def Importance(self, arg ,dataset : pd.DataFrame) -> tuple:
        numOfNotClassifiableRows = 0
        currDataFrame = dataset[[arg,self.outputAtt]]
        values = self.valuesOfColumn(currDataFrame,arg)
        for val in values:
            rows = self.filterDataframe(dataset,arg,val)
            outputs = rows.nunique('index')
            if outputs[len(outputs)-1] > 1:
                numOfNotClassifiableRows += len(rows.index)
        return (arg,numOfNotClassifiableRows)
    
    #Devuelve el atributo que clasifique la mayor cantidad de filas.
    def mostImportantArgument(self, dataset : pd.DataFrame, attributes : list):
        mostImportant = (attributes[0],len(dataset.index))
        for i in range(0,len(attributes)):
            a = attributes[i]
            if a != self.outputAtt:
                currentImportance = self.Importance(a,dataset)
                if mostImportant[1] > currentImportance[1] or (mostImportant[1] == currentImportance[1] and random.choice([True,False])):
                    mostImportant = currentImportance  
        return mostImportant[0]

    def addBranch(self,tree : t.Tree,subtree : t.Node|t.Tree,value):
        parent = tree.get_node(tree.root) 
        if(isinstance(subtree,t.Tree)):
            #addbranch
            subRoot = subtree.get_node(subtree.root)
            tree.create_node(tag=str([value,subRoot.tag]),identifier=value,parent=parent.identifier,data=subRoot.data)
            tree.merge(value,subtree)
        elif(isinstance(subtree,t.Node)):
            #addNode
            subRoot = subtree
            tree.create_node(tag=str([value,subRoot.data]),identifier=value,parent=parent.identifier,data=subRoot.data)
            
    def recursiveTree(self,examples : pd.DataFrame,attributes : list,parentExample : pd.DataFrame) -> t.Tree | t.Node:
        if(len(examples.index) == 0):
            return self.plularityValue(parentExample)
        elif(self.countOutputValues(examples) == 1):
            return self.getUniqueOutput(examples)
        elif(len(attributes) == 0):
            return self.plularityValue(examples)
        else:
            A = self.mostImportantArgument(examples,attributes)
            tree = self.newTree(A)
            attributes.remove(A)
            for vk in self.valuesOfColumn(examples,A):
                newExamples = self.filterDataframe(examples,A,vk)
                subtree = self.recursiveTree(newExamples, attributes, examples)
                self.addBranch(tree,subtree,vk)
        return tree

    def decisionTreeLearning(self,examples : pd.DataFrame) -> t.Tree:
        tree = self.recursiveTree(examples,examples.columns.tolist(),examples)
        if(isinstance(tree,t.Tree)):
            return tree
        else:
            return t.Tree()

    def applyModel(self,row : pd.DataFrame,attributes : list, tree : t.Tree):
        currentNode = tree.get_node(tree.root)
        i = 0
        while( i < len(attributes)):
            if(attributes[i] == currentNode.data):
                value = row.iat[i]
                child = tree.get_node(value)
                if child.data in attributes:
                    currentNode = child
                    i = -1
                else:
                    return child.data
            i+=1
        return None

    def test(self,test : pd.DataFrame, treeModel : t.Tree) -> pd.DataFrame:
        resultArr = []
        for index in test.index:
            row =  test.loc[index]
            result = self.applyModel(row,test.columns.tolist(),treeModel)
            resultArr.append(result)
        test[self.outputAtt] = resultArr
        return test

