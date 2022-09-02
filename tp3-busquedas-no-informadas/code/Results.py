import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Results:
    index=0
    
    def __init__(self,head):
        self.resultSet = pd.DataFrame(columns=head)
        self.path = None
    
    def addRegister(self,register):
        self.resultSet.loc[self.index] = register
        self.index+=1

    def makeCSV(self,path):
        self.path=path
        pd.DataFrame.to_csv(self.resultSet,path)

    def plotBoxDiagram(self,x,y):
        plt.show()
        sns.catplot(x,y,kind="box",data=self.resultSet)
        plt.show(block = True)

    def plotBoxDiagram(self,x,y,hue):
        plt.show()
        sns.catplot(x,y,hue,kind="box",data=self.resultSet)
        plt.show(block = True)

    def plotBoxDiagram(self,x,y,col):
        plt.show()
        sns.catplot(x,y,col,kind="box",data=self.resultSet)
        plt.show(block = True)

    def plotBoxDiagram(self,x,y,hue,col):
        plt.show()
        sns.catplot(x,y,hue,col,kind="box",data=self.resultSet)
        plt.show(block = True)

    def savePlot(fileName):
        plt.savefig( fileName + ".png")
    
    def savePlot(path,fileName):
        plt.savefig(path + "\\" + fileName + ".png")
        