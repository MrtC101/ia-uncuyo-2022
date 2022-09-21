import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from threading import Lock
class Results:
    index=0
    mutex = Lock()

    def __init__(self,head):
        self.resultSet = pd.DataFrame(columns=head)
        self.path = None
    
    def dataAnalysis(self,AnalysisfileName):
        all = self.resultSet.size
        solType = pd.unique(self.resultSet["Algorithm"])
        solSubGroup = self.resultSet.groupby("Algorithm") 
        for j in range(0,len(solType)):
            solSub = solSubGroup.get_group(solType[j])
            sizeGroups = pd.unique(solSub["Size"])
            sizeSubGroup = solSub.groupby("Size")
            for i in range(0,len(sizeGroups)):
                subgroup = sizeSubGroup.get_group(sizeGroups[i])
                with open(AnalysisfileName,'a') as file:
                    file.write("===\nData Analysis\n")
                    file.write("Mean:\n")
                    file.write(str(subgroup.mean(axis='index',numeric_only=True))+"\n")
                    file.write("Starndar Deviation:\n")
                    file.write(str(subgroup.std(axis='index',ddof=0,numeric_only=True))+"\n")
                    file.write("Percentage of optimal solution: ")
                    solutions =  subgroup[subgroup["Threatened_Queens"]==0]
                    solutionNumber = solutions.size
                    file.write(str(solutionNumber/all) + "\n")
            
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
        self.mutex.acquire()
        self.resultSet.loc[self.index] = register
        self.index+=1
        self.mutex.release()

    def plotBoxDiagram1(self,x,y):
        plt.show(block = False)
        sns.catplot(x=x,y=y,kind="box",data=self.resultSet)
        plt.show(block = False)

    def plotBoxDiagram2(self,x,y,hue):
        plt.show(block = False)
        sns.catplot(x=x,y=y,hue=hue,kind="box",data=self.resultSet)
        plt.show(block = False)

    def plotBoxDiagram3(self,x,y,col):
        plt.show(block = False)
        sns.catplot(x=x,y=y,col=col,kind="box",data=self.resultSet)
        plt.show(block = False)

    def plotBoxDiagram4(self,x,y,hue,col):
        plt.show(block = False)
        sns.catplot(x=x,y=y,hue=hue,col=col,kind="box",data=self.resultSet)
        plt.show(block = False)

    def plotBoxDiagramSubgroup(self,x,y,hue,col,subgroup):
        plt.show(block = False)
        sns.catplot(x=x,y=y,hue=hue,col=col,kind="box",data=subgroup)
        plt.show(block = False)

    def savePlot(self,fileName):
        plt.savefig( fileName + ".png")
    
    def Union(self,dataSet):
        self.resultSet = pd.concat([self.resultSet,dataSet])
    """
    Extraer un subconjunto
    dt = rs.Results(["Solution_was_found","Algorithm","Obstacles_rate","Solution_Lenght","Amount_of_explored_states"])
    dt.loadCSV("tp3-SameEnvironment-resultSet.csv")
    subgroup = dt.resultSet
    subgroup = subgroup[subgroup["Algorithm"] != "DFS"]
    dt.plotBoxDiagramSubgroup(x="Solution_Lenght",y="Algorithm",hue="Solution_was_found",col="Obstacles_rate",subgroup=subgroup)
    dt.savePlot(fileName="BoxPlotBestSolution-three")
    """