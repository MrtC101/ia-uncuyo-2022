from Simulation import Simulation
import Results as rs
from enums import Solution
import math
import threading

if __name__== "__main__":
    #params
    problemSize = 4
    simType = Solution.SIMM_ANNEALING
    #Ejecucion
    if simType == Solution.RunAll:
        iterations = 1
        threadNumber = 12
        resultSet = rs.Results(["Algorithm","Size","Threatened_Queens","Amount_of_explored_states","Time"])
        #THREADS
        simAr = list()
        for i in range(0,threadNumber):
            start =  math.floor(iterations * i / threadNumber)
            end =  math.floor(iterations * (i+1) / threadNumber)
            numberOfIter = end-start
            if(numberOfIter>0):
                thread = threading.Thread(target = Simulation.startSimulation, args = (resultSet,problemSize,numberOfIter))
                thread.start()
                simAr.append(thread)
        for i in range(0,len(simAr)):        
            if(simAr[i].joinable()):
                simAr[i].join()
        #RESUlTS
        resultSet.makeCSV(path=".\\ResultSet\\tp5-resultSet.csv")
        resultSet.dataAnalysis(AnalysisfileName=".\\ResultSet\\DataAnalysis.txt")
        resultSet.plotBoxDiagram(x="Amount_of_explored_states",y="Algorithm",hue=None,col="size")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot")
    elif simType == Solution.HILL_CLIMBING:
        Simulation.startSimulation(problemSize,Solution.HILL_CLIMBING)
    elif simType == Solution.SIMM_ANNEALING:
        Simulation.startSimulation(problemSize,Solution.SIMM_ANNEALING)
    elif simType == Solution.GENETIC:
        Simulation.startSimulation(problemSize,Solution.GENETIC)
    
    