from Environment import *
from Agent import *
from enums import Solution

class Simulation:

    def __init__(self,size):
        self.env = Environment(size)
        self.agent = Agent(self.env)

    def printSolution(self,solutionTuple):
        print("Cantidad de Estados Visitados:",solutionTuple[1])
        print("Cantidad de reinas amenazadas",solutionTuple[0][1])
        print("Tablero Inicial:")
        self.env.print_enviroment()
        print("Tablero Solicion:")
        self.env.print_enviroment(solutionTuple[0][0])
    
    def run(self,solutionType):
        if solutionType == Solution.HILL_CLIMBING:
            solution = self.agent.hill_climbing()
        elif solutionType == Solution.SIMM_ANNEALING:
            solution = self.agent.simmulated_annealing()
        elif solutionType == Solution.GENETIC:
            solution = self.agent.simmulated_annealing()
        else:
            raise Exception("No type solution was selected.")
        return solution

    def runAll(self):
        resultArr = []
        for sol in Solution:
            self.resetStateVisitedAmount()
            startTime = Time.time()
            state = self.run(sol)
            endTime = Time.time()
            resultArr.append(state[0],state[1],self.getStatesVisitedAmount(),endTime-startTime)
        return resultArr
    
    def startSimulation(size,solutionType):
        currSim = Simulation(size)
        solution = currSim.run(solutionType)
        currSim.printSolution(solution)

    def startSimulation(resultSet,size,iterNumber):
        for i in range(0,iterNumber):
            currSim = Simulation(size)
            resultArr = currSim.runAll()
            for i in range(0,len(resultArr)):
                register = [Solution(i).name,size,resultArr[i][1],resultArr[i][2],resultArr[i][3]]
                resultSet.addRegister(register)

    