from Simulation import Simulation
import Results as rs
from Solution import Solution,Option
import time
import threading
def startSimulation(resultSet,size,obstacles_rate,solutionType,option):
    
    currSim = Simulation(size,obstacles_rate)
    if solutionType == Solution.SameEnvironment:
        result = currSim.runAll()
        for i in range(0,len(result),2):
            if isinstance(result[i],str):
                found = "No"
                size = 0
            else:
                found = "Yes"
                size = len(result[i])
            if i==0:
                algo = Solution.BFS
            elif i==2:
                algo = Solution.DFS
            elif i==4:
                algo = Solution.DFSLimited
            elif i==6:
                algo = Solution.UniformCost
            register = [found, algo.name,obstacles_rate,size,result[i+1]]
            resultSet.addRegister(register)
    else:
        if option == Option.NoGraphics:
            result = currSim.run(solutionType) 
        else:
            currSim.runWithGraphic(solutionType)
            return
        if isinstance(result,str):
            found = "No"
            size = 0
        else:
            found = "Yes"
            size = len(result)
        register = [found, solutionType.name,obstacles_rate,len(result),currSim.get_Performance()]
        resultSet.addRegister(register)

#Trada debido al DFS
if __name__== "__main__":
    start = time.time()
    #params
    iter = 30
    size = 100
    obstacles_rate = 0.1
    simType = Solution.SameEnvironment

    resultSet = rs.Results(["Solution_was_found","Algorithm","Obstacles_rate","Solution_Lenght","Amount_of_explored_states"])
    if simType == Solution.SameEnvironment:
        #the same evironment
         for j in range(0,iter):
            sim = threading.Thread(target = startSimulation, args = (resultSet,size,obstacles_rate,simType,Option.NoGraphics))
            sim.start()
            sim.join()
    elif simType == Solution.RandomEnvironment:
        #diferent ecironment
        for j in range(0,iter*3):
            if j == 0:
                solutionType =Solution.BFS
            if j == iter:
                solutionType =Solution.DFS
            if j == iter*2:
                solutionType =Solution.UniformCost
            sim = threading.Thread(target = startSimulation, args = (resultSet,size,obstacles_rate,solutionType,Option.NoGraphics))
            sim.start()
            sim.join()
    elif simType == Solution.BFS:
        startSimulation(resultSet,size,obstacles_rate,Solution.BFS,Option.WhithGraphics)
    elif simType == Solution.DFS:
        startSimulation(resultSet,size,obstacles_rate,Solution.DFS,Option.WhithGraphics)
    elif simType == Solution.DFSLimited:
        startSimulation(resultSet,size,obstacles_rate,Solution.DFSLimited,Option.WhithGraphics)
    elif simType == Solution.UniformCost:
        startSimulation(resultSet,size,obstacles_rate,Solution.UniformCost,Option.WhithGraphics)
    #persistance
    if simType == Solution.RandomEnvironment or simType == Solution.SameEnvironment:
        resultSet.makeCSV(path="tp3-"+simType.name+"-resultSet.csv")
        resultSet.dataAnalysis(AnalysisfileName="DatAnalysis.txt")
        resultSet.plotBoxDiagram(x="Amount_of_explored_states",y="Algorithm",hue="Solution_was_found",col="Obstacles_rate")
        resultSet.savePlot(fileName="BoxPlotFaster-"+simType.name)
        resultSet.plotBoxDiagram(x="Solution_Lenght",y="Algorithm",hue="Solution_was_found",col="Obstacles_rate")
        resultSet.savePlot(fileName="BoxPlotBestSolution-"+simType.name)

    end = time.time()
    print(end-start)
    