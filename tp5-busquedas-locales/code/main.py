from Simulation import Simulation
import Results as rs
import time
from enums import Solution
import threading

def code(resultSet,problemSize,iterations):
    #THREADS
    Simulation.startSimulationThread(resultSet,problemSize,iterations)
    
if __name__== "__main__":
    #params
    problemSize = 15
    simType = "RunAll"
    start = time.time()
    #Ejecucion
    if simType == "RunAll":
        probleSizeArr =[4,8,10,12,15]
        iterations = 30
        resultSet = rs.Results(["Algorithm","Size","Threatened_Queens","Amount_of_explored_states","Time"])
        simAr = list()
        for i in range(0,len(probleSizeArr)):
            problemSize = probleSizeArr[i]
            thread = threading.Thread(target = code , args =(resultSet,problemSize,iterations))
            thread.start()
            simAr.append(thread)
        for i in range(0,len(simAr)):
            if(simAr[i].is_alive()):
                simAr[i].join()
        #RESUlTS
        resultSet.makeCSV(path=".\\ResultSet\\tp5-resultSet.csv")
        resultSet.dataAnalysis(AnalysisfileName="TP5-reporte.md")
        resultSet.plotBoxDiagram3(x="Algorithm",y="Amount_of_explored_states",col="Size")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot-ExploredStates")
        resultSet.plotBoxDiagram3(x="Algorithm",y="Time",col="Size")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot-Time")
        resultSet.plotBoxDiagram3(x="Algorithm",y="Threatened_Queens",col="Size")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot-ThreatenedQueens")
    elif simType == Solution.HILL_CLIMBING:
        Simulation.startSimulation(problemSize,Solution.HILL_CLIMBING)
    elif simType == Solution.SIM_ANNEALING:
        Simulation.startSimulation(problemSize,Solution.SIM_ANNEALING)
    elif simType == Solution.GENETIC:
        Simulation.startSimulation(problemSize,Solution.GENETIC)
    end = time.time()
    print(end-start)    
    