from Environment import *
from Agent import *
from enums import Solution
import random

class Simulation:

    def __init__(self,size):
        self.env = Environment(size)
        self.agent = Agent(self.env)


    def runAll(self):
        result = []
        result.append(self.agent.hill_climbing())
        result.append(self.agent.getStatesVisitedAmount())
        result.append(self.agent.simmulated_annealing())
        result.append(self.agent.getStatesVisitedAmount())
        return result

    def run(self,solutionType):
        if solutionType == Solution.HILL_CLIMBING:
            solution = self.agent.hill_climbing()
        if solutionType == Solution.SIMM_ANNEALING:
            solution = self.agent.simmulated_annealing()
        else:
            raise Exception("No posible solution was selected.")
        return solution
    
    def printSolution(self,arr):
        if isinstance(arr,str):
            print(arr)
        else:
            print("[",end="")
            for i in range(0,len(arr)):
                print(arr[i],end="")
                if i != len(arr)-1:
                    print("",end=",")
            print("]")
        ##
            for i in range (len(arr[0])-1,-1,-1):
                for j in range (0,len(arr[0])):
                    if(arr[0][j]==i):
                        print("|<>",end="")
                    else:
                        print("|  ",end="")
                print("|")
            print()

    def runWithGraphic(self,solutionType):
        self.env.print_enviroment()
        solution = self.run(solutionType)
        print(self.get_Performance())
        self.printSolution(solution)


    def get_Performance(self):
        return self.agent.getStatesVisitedAmount()