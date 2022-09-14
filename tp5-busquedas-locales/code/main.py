from Simulation import Simulation
import Results as rs
from enums import Solution,Option
import time
import threading

def startSimulation(resultSet,size,solutionType,option):
    currSim = Simulation(size)
    
    if solutionType == Solution.RunAll:
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
            elif i==8:
                algo = Solution.AEstrella
            register = [found, algo.name,size,result[i+1]]
            resultSet.addRegister(register)
    else:
        if option == Option.NoGraphics:
            result = currSim.run(solutionType) 
        else:
            currSim.runWithGraphic(solutionType)
            return
        if isinstance(result,str):
            found = "No"
        else:
            found = "Yes"
        register = [found, solutionType.name,size,result[1],currSim.get_Performance()]
        resultSet.addRegister(register)
    

#Trada debido al DFS
if __name__== "__main__":
    start = time.time()
    #params
    iter = 1
    size = 4
    simType = Solution.SIMM_ANNEALING
    resultSet = rs.Results(["Solution_was_found","Algorithm","Size","Value","Amount_of_explored_states"])

    if simType == Solution.RunAll:
        #the same evironment
        for j in range(0,iter):
            sim = threading.Thread(target = startSimulation, args = (resultSet,size,simType,Option.NoGraphics))
            sim.start()
            sim.join()
    elif simType == Solution.HILL_CLIMBING:
        startSimulation(resultSet,size,Solution.HILL_CLIMBING,Option.WhithGraphics)
    elif simType == Solution.SIMM_ANNEALING:
        startSimulation(resultSet,size,Solution.SIMM_ANNEALING,Option.WhithGraphics)
    """
    
    resultSet.makeCSV(path="tp4-resultSet.csv")
    resultSet.dataAnalysis(AnalysisfileName="DataAnalysis.txt")
    resultSet.plotBoxDiagram(x="Amount_of_explored_states",y="Algorithm",hue="Solution_was_found",col="Obstacles_rate")
    resultSet.savePlot(fileName="BoxPlotFaster-A")
    resultSet.plotBoxDiagram(x="Solution_Lenght",y="Algorithm",hue="Solution_was_found",col="Obstacles_rate")
    resultSet.savePlot(fileName="BoxPlotBestSolution-A")
    subgroup = resultSet.resultSet
    subgroup = subgroup[subgroup["Algorithm"] != "DFS"]
    resultSet.plotBoxDiagramSubgroup(x="Solution_Lenght",y="Algorithm",hue="Solution_was_found",col="Obstacles_rate",subgroup=subgroup)
    resultSet.savePlot(fileName="BoxPlotBestSolution-four")
    """
    end = time.time()
    print(end-start)
    