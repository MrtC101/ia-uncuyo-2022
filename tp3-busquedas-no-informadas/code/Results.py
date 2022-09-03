import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Results:
    index=0
    
    def __init__(self,head):
        self.resultSet = pd.DataFrame(columns=head)
        self.path = None
    
    def dataAnalysis(self):
        print("Mean:")
        print(str(self.getMean()))
        print("Starndar Deviation:")
        print(str(self.getStandarDeviation()))

    def getMean(self):
        return self.resultSet.mean(axis='index',numeric_only=True)

    def getVariance(self):
        return self.resultSet.var(axis='index',ddof=0,numeric_only=True)
    
    def getStandarDeviation(self):
        return self.resultSet.std(axis='index',ddof=0,numeric_only=True)

    def loadCSV(self,path):
        self.resultSet = pd.read_csv(path)
    
    def makeCSV(self,path):
        self.path=path
        pd.DataFrame.to_csv(self.resultSet,path)

    def addRegister(self,register):
        self.resultSet.loc[self.index] = register
        self.index+=1

    def plotBoxDiagram(self,x,y):
        plt.show(block = False)
        sns.catplot(x=x,y=y,kind="box",data=self.resultSet)
        plt.show(block = False)

    def plotBoxDiagram(self,x,y,hue):
        plt.show(block = False)
        sns.catplot(x=x,y=y,hue=hue,kind="box",data=self.resultSet)
        plt.show(block = False)

    def plotBoxDiagram(self,x,y,col):
        plt.show(block = False)
        sns.catplot(x=x,y=y,col=col,kind="box",data=self.resultSet)
        plt.show(block = False)

    def plotBoxDiagram(self,x,y,hue,col):
        plt.show(block = False)
        sns.catplot(x=x,y=y,hue=hue,col=col,kind="box",data=self.resultSet)
        plt.show(block = False)

    def savePlot(self,fileName):
        plt.savefig( fileName + ".png")
        