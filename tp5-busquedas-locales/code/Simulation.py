from Environment import *
from Agent import *
import time
from enums import Solution

class Simulation:

    def __init__(self,size):
        self.env = Environment(size)
        self.agent = Agent(self.env)

    def printSolution(self,solution):
        print("Cantidad de Estados Visitados: ",self.agent.getStatesVisitedAmount())
        print("Cantidad de reinas amenazadas: ",solution[1])
        print("Tablero Inicial:")
        self.env.print_enviroment()
        print("Tablero Solicion:")
        Environment.print_enviromentExtern(solution[0])
    
    def run(self,solutionType):
        if solutionType == Solution.HILL_CLIMBING.name:
            solution = self.agent.hill_climbing()
        elif solutionType == Solution.SIM_ANNEALING.name:
            solution = self.agent.simulated_annealing()
        elif solutionType == Solution.GENETIC.name:
            solution = self.agent.genetic_algorithm()
        return solution

    def runAll(self):
        resultArr = []
        for sol in Solution:
            self.agent.resetStateVisitedAmount()
            startTime = time.time()
            state = self.run(sol.name)
            endTime = time.time()
            resultArr.append((state[0],state[1],self.agent.getStatesVisitedAmount(),endTime-startTime))
        return resultArr
    
    def startSimulation(size,solutionType):
        currSim = Simulation(size)
        solution = currSim.run(solutionType.name)
        currSim.printSolution(solution)

    def startSimulationThread(resultSet,size,iterNumber):
        for i in range(0,iterNumber):
            currSim = Simulation(size)
            resultArr = currSim.runAll()
            for i in range(0,len(resultArr)):
                register = [Solution(i+1).name,size,resultArr[i][1],resultArr[i][2],resultArr[i][3]]
                resultSet.addRegister(register)

    