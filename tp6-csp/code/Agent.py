from sys import excepthook
import treelib as t
from random import randint,choices, random
from enums import Move
import math

class Agent:
    
    #resive como parametro un objeto Environment
    def __init__(self,env):
        self.env = env
        self.statesVisitedAmount = 0
        self.foward = False

    def resetStateVisitedAmount(self):
        self.statesVisitedAmount = 0

    def getStatesVisitedAmount(self):
        return self.statesVisitedAmount

    def __addStatesVisitedAmount(self):
        self.statesVisitedAmount+=1
    
    def __addToStatesAmount(self,i):
        self.statesVisitedAmount+=i

    def __getRightPos(self,queenPos,direction,currX):
        if(direction==Move.UPDiag):
            return (currX,queenPos[1]+(queenPos[0]-currX))
        elif(direction==Move.RIGHT):
            return (currX,queenPos[1])
        elif(direction==Move.DOWNDiag):
            return (currX,queenPos[1]-(queenPos[0]-currX))

    def __getLeftPos(self,queenPos,direction,currX):
        if(direction==Move.UPDiag):
            return (currX,queenPos[1]+(queenPos[0]-currX))
        elif(direction==Move.LEFT):
            return (currX,queenPos[1])
        elif(direction==Move.DOWNDiag):
            return (currX,queenPos[1]-(queenPos[0]-currX))

    def __is_inside(self,state):
        if state[0] < self.env.size and state[0]>-1 and state[1] < self.env.size and state[1]>-1:
            return True
        return False
    #
    def __checkQueen(self,state):
        checkedNum = 0
        hashTable = {}
        moveArr = {Move.UPDiag,Move.LEFT,Move.DOWNDiag}
        checked = {}
        #por cada reina
        for i in range(0,len(state)):
            for move in moveArr:
                checked[move.name] = False
            queenPos = (i,state[i])
            hashTable[str(queenPos)] = False
            #revisar las columnas anteriores
            for j in range(i-1,-1,-1):
                for move in moveArr: 
                    if(checked[move.name]==False):
                        nextPos = self.__getLeftPos(queenPos,move,j)
                        if self.__is_inside(nextPos):
                            if hashTable.get(str(nextPos)) != None:
                                if(hashTable[str(queenPos)] == False):
                                    checkedNum += 1
                                    hashTable[str(queenPos)] = True
                                if(hashTable[str(nextPos)] == False):
                                    checkedNum += 1
                                    hashTable[str(nextPos)] = True
                                checked[move.name] = True
        return checkedNum
    
#----------------------------------------------------------------------#
    def heuristic(self,state,currVar):
        checkedNum = 0
        moveArr = {Move.UPDiag,Move.LEFT,Move.DOWNDiag}
        checked = {}
        #por cada reina
        for move in moveArr:
            checked[move.name] = False
        queenPos = (currVar,state[currVar])
        #revisar las columnas anteriores
        for j in range(currVar-1,-1,-1):
            for move in moveArr: 
                if(checked[move.name]==False):
                    nextPos = self.__getLeftPos(queenPos,move,j)
                    if self.__is_inside(nextPos):
                        if((j,state[j])==nextPos):
                            checkedNum += 1
                            checked[move.name] = True
        return checkedNum

    def restrictDomains(self,domain,state,currVar):
        moveArr = {Move.UPDiag,Move.RIGHT,Move.DOWNDiag}
        skip = False
        oldtable = domain[0]
        newDomain = []
        for i in range(0,len(oldtable)):
            col = []
            for j in range(0,len(oldtable[i])):
                col.append(oldtable[i][j])
            newDomain.append(col)
        queenPos = (currVar,state[currVar])
        #revisar las columnas anteriores
        for j in range(currVar+1,self.env.size):
            for move in moveArr: 
                nextPos = self.__getRightPos(queenPos,move,j)
                if self.__is_inside(nextPos):
                    if newDomain[nextPos[0]].count(nextPos[1]) > 0:
                        newDomain[nextPos[0]].remove(nextPos[1])
            if self.foward:
                if len(newDomain[nextPos[0]]) == 0:
                    skip = True
                    break;
        return (newDomain,skip)

    def backtrack(self,currSolution,domain,currentVar):
        if currentVar == self.env.size:
            h = self.__checkQueen(currSolution[0])
            if h == 0:
                return (currSolution[0],h)
            else:
                return False
        table = currSolution[0].copy()
        for val in domain[0][currentVar]:
            self.__addStatesVisitedAmount()    
            table[currentVar] = val
            if self.heuristic(table,currentVar) == 0:
                newdomain = self.restrictDomains(domain,table,currentVar)
                if not newdomain[1]:
                    newSolution = (table,self.env.size)
                    newSolution = self.backtrack(newSolution,newdomain,currentVar+1)    
                    if newSolution != False:
                        return newSolution
        return False

    def backtrackingSearch(self,foward):
        self.foward = foward
        solution = (self.env.table,self.__checkQueen(self.env.table))
        domain = (self.env.domain,False)
        return self.backtrack(solution,domain,0)
#----------------------------------------------------------------------#
