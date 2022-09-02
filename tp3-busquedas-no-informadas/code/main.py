from Simulation import Simulation
import Results as rs
from Solution import Solution
import threading


def startSimulation(resultSet,size,obstacles_rate,solutionType):
    currSim = Simulation(size,obstacles_rate)
    result = currSim.run(solutionType)
    if result == None:
        found = "No"
    else:
        found = "Yes"
    register = [found, solutionType.name,obstacles_rate] + [currSim.get_Performance()]
    resultSet.addRegister(register)

if __name__== "__main__":
    path="tp3-resultSet.csv"
    iter = 30
    size = 100
    obstacles_rate = 0.1
    resultSet = rs.Results(["Solution_was_found","Algorithm","Obstacles_rate","Amount_of_explored_states"])
    for j in range(0,iter): 
       sim1 = threading.Thread(target = startSimulation, args = (resultSet,size,obstacles_rate,Solution.BFS))
       sim1.start()
       sim1.join()
    for j in range(0,iter): 
       sim1 = threading.Thread(target = startSimulation, args = (resultSet,size,obstacles_rate,Solution.DFS))
       sim1.start()
       sim1.join()
    for j in range(0,iter): 
       sim1 = threading.Thread(target = startSimulation, args = (resultSet,size,obstacles_rate,Solution.UniformCost))
       sim1.start()
       sim1.join()
    resultSet.makeCSV(path)
    resultSet.plotBoxDiagram(x="Amount_of_explored_states",y="Algorithm",hue="Solution_was_found",col="Obstacles_rate")
    resultSet.savePlot("BoxPlot")