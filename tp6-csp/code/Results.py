from sqlite3 import Row
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
    
    def serieString(self,serie):
        values = serie.array
        axes = serie.axes[0]
        rep = "<ul>"
        for i in range(1,len(values)):
            rep +="<li>"+ axes[i] +" = "+ str(round(values[i],3)) + "\n\n"+ "</li>"
        return rep + "</ul>"
    
    def dataAnalysis(self,AnalysisfileName):
        all = self.resultSet.size
        table = "<table><caption>Results</caption>"
        table += "<thead>"
        table +=    "<tr>"
        table +=        "<th>Size</th>"
        table +=        "<th>Hill Climbing</th>"
        table +=        "<th>Simmulated Annealing</th>"
        table +=        "<th>Genetic Algorithm</th>"
        table +=    "</tr>"
        table += "</thead>"
        table += "<tbody>";
        sizeGroups = pd.unique(self.resultSet["Size"])
        sizeSubGroup = self.resultSet.groupby("Size")
        for i in range(0,len(sizeGroups)):
            table +="<tr>"
            table += "<td>"+str(sizeGroups[i])+"</td>"
            sizeSol = sizeSubGroup.get_group(sizeGroups[i])
            solType = pd.unique(sizeSol["Algorithm"])
            solSubGroup = sizeSol.groupby("Algorithm") 
            for j in range(0,len(solType)):
                subgroup = solSubGroup.get_group(solType[j])
                solutions =  subgroup[subgroup["Threatened_Queens"]==0]
                solutionNumber = solutions.size
                table +="<td>"
                table +="Mean:\n\n"
                table +=self.serieString(subgroup.mean(axis='index',numeric_only=True))
                table +="Starndar Deviation:\n\n"
                table +=self.serieString(subgroup.std(axis='index',ddof=0,numeric_only=True))
                table +="Percentage of optimal solutions = "
                table +=str(round(solutionNumber/all,3)) + "\n"
                table +="</td>"
            table +="</tr>"
        with open(AnalysisfileName,'a') as file:
            file.write(table +"</tbody>"+"</table>")
                
    def getMean(self):
        return self.resultSet.mean(axis='index',numeric_only=True)

    def getVariance(self):
        return self.resultSet.var(axis='index',ddof=0,numeric_only=True)
    
    def getStandarDeviation(self):
        return self.resultSet.std(axis='index',ddof=0,numeric_only=True)

    def loadCSV(self,path):
        labels = self.resultSet.axes[1]
        self.resultSet = pd.read_csv(path,usecols=labels)
        self.index = len(self.resultSet)-1
    
    def makeCSVWrite(self,path):
        self.path=path
        pd.DataFrame.to_csv(self.resultSet,path,mode="w")

    def makeCSVAppend(self,path): 
        self.path=path
        pd.DataFrame.to_csv(self.resultSet,path,header=False,mode="a")

    def addRegister(self,register):
        self.mutex.acquire()
        self.resultSet.loc[self.index] = register
        self.index+=1
        self.mutex.release()

    def plotDisDiagram(self,x,y,hue):
        plt.show(block = False)
        sns.relplot(x=x,y=y,hue=hue,kind="line",data=self.resultSet)
        plt.show(block = False)

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