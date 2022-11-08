from Environment import *
from Agent import *
from Solution import Solution
import random

class Simulation:

    def __init__(self,size,obstacles_rate):
        agentX=random.randint(0,size-1)
        agentY=random.randint(0,size-1)
        while True:
            goalX=random.randint(0,size-1)
            goalY=random.randint(0,size-1)
            if goalX!=agentX or goalY!=agentY:
                break
        self.env = Environment(size,size,agentX,agentY,goalX,goalY,obstacles_rate)
        self.agent = Agent(self.env)
    
    def comparePerformance(self,per1,per2):
        if per1 < per2:
            return True
        return False

    def compareSolution(self,sol1,sol2):
        if isinstance(sol1,str):
            return False
        if isinstance(sol2,str):
            return False
        if len(sol1)<len(sol2):
            return True
        return False

    def runAll(self):
        result = []
        result.append(self.agent.solveByBFS())
        result.append(self.agent.getStatesVisitedAmount())
        result.append(self.agent.solveByDFS())
        result.append(self.agent.getStatesVisitedAmount())
        result.append(self.agent.solveByDFSLimited())
        result.append(self.agent.getStatesVisitedAmount())
        result.append(self.agent.solveByUniformCost())
        result.append(self.agent.getStatesVisitedAmount())
        return result
        
    def run(self,solutionType):
        if solutionType == Solution.BFS:
            solution = self.agent.solveByBFS()
        elif solutionType == Solution.DFS:
            solution = self.agent.solveByDFS()
        elif solutionType == Solution.DFSLimited:
            solution = self.agent.solveByDFSLimited()
        elif solutionType == Solution.UniformCost:
            solution = self.agent.solveByUniformCost()
        else:
            raise Exception("No posible solution was selected.")
        return solution

    def printSolution(self,arr):
        if isinstance(arr,str):
            print(arr)
        else:
            print("[",end="")
            for i in range(0,len(arr)):
                print(arr[i].tag,end="")
                if i != len(arr)-1:
                    print("",end=",")
            print("]")

    def runWithGraphic(self,solutionType):
        self.env.print_enviroment()
        solution = self.run(solutionType)
        self.printSolution(solution)

    def get_Performance(self):
        return self.agent.getStatesVisitedAmount()