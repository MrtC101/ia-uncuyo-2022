import treelib as t
from random import randint,choices, random
from enums import Move
import math

class Agent:
    
    #resive como parametro un objeto Environment
    def __init__(self,env):
        self.env = env
        self.arrH = []
        self.statesVisitedAmount = 0

    def resetStateVisitedAmount(self):
        self.statesVisitedAmount = 0

    def getStatesVisitedAmount(self):
        return self.statesVisitedAmount

    def __addStatesVisitedAmount(self):
        self.statesVisitedAmount+=1
    
    def __addToStatesAmount(self,i):
        self.statesVisitedAmount+=i

    def __getNextPos(self,queenPos,direction,currX):
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
                        nextPos = self.__getNextPos(queenPos,move,j)
                        if self.__is_inside(nextPos):
                            if hashTable.get(str(nextPos)) != None:
                                if(hashTable[str(queenPos)] == False):
                                    checkedNum += 1
                                    hashTable[str(queenPos)] = True
                                if(hashTable[str(nextPos)] == False):
                                    checkedNum += 1
                                    hashTable[str(nextPos)] = True
                                checked[move.name] = True
        self.arrH.append(checkedNum)
        return checkedNum
#----------------------------------------------------------------------#
    def VueltaRecursiva(self,max):
        current = (self.env.table,self.__checkQueen(self.env.table))
        if current[1] == 0:
            return current
        else:
            

    def BusquedaConVuelta():
        solution = VueltaRecursiva(30)
        return solution