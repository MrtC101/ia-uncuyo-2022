from genericpath import isfile
from pydoc import ispath
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
    problemSize = 10
    simType = "RunAll"
    start = time.time()
    #Ejecucion
    if simType == "RunAll":
        probleSizeArr = [4,8,10]
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
        resultSet.makeCSVWrite(path=".\\ResultSet\\tp5-resultSet.csv")
        resultSet.dataAnalysis(AnalysisfileName="TP5-reporte.md")
        resultSet.plotBoxDiagram3(x="Algorithm",y="Amount_of_explored_states",col="Size")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot-ExploredStates")
        resultSet.plotBoxDiagram3(x="Algorithm",y="Time",col="Size")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot-Time")
        resultSet.plotBoxDiagram3(x="Algorithm",y="Threatened_Queens",col="Size")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot-ThreatenedQueens")
    elif simType == Solution.HILL_CLIMBING:
        resultSet = rs.Results(["Algorithm","Size","h_functionValue"])
        if(isfile(".\\ResultSet\\tp5-functions.csv")):
            resultSet.loadCSV(path=".\\ResultSet\\tp5-functions.csv")
        Simulation.startSimulation(problemSize,Solution.HILL_CLIMBING,resultSet)
    elif simType == Solution.SIM_ANNEALING:
        resultSet = rs.Results(["Algorithm","Size","h_functionValue"])
        if(isfile(".\\ResultSet\\tp5-functions.csv")):
            resultSet.loadCSV(path=".\\ResultSet\\tp5-functions.csv")
        Simulation.startSimulation(problemSize,Solution.SIM_ANNEALING,resultSet)
    elif simType == Solution.GENETIC:
        resultSet = rs.Results(["Algorithm","Size","State","It","Value"])
        Simulation.startSimulation(problemSize,Solution.GENETIC,resultSet)
    
    if(simType == Solution.GENETIC):
        resultSet.makeCSVWrite(path=".\\ResultSet\\tp5-thicness.csv")
        resultSet.plotDisDiagram(x="It",y="Value",hue="State")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot-thicness")
    else:
        resultSet.makeCSVWrite(path=".\\ResultSet\\tp5-functions.csv")
        resultSet.plotBoxDiagram3(x="Algorithm",y="h_functionValue",col="Size")
        resultSet.savePlot(fileName=".\\ResultSet\\BoxPlot-h_Function")
    end = time.time()
    print(end-start)    
    