import treelib as t
from random import randint,choices
from enums import Move
import math

class Agent:
    #resive como parametro un objeto Environment
    def __init__(self,env):
        self.env = env
        self.statesVisitedAmount = 0

    def resetStateVisitedAmount(self):
        self.statesVisitedAmount = 0

    def getStatesVisitedAmount(self):
        return self.statesVisitedAmount

    def __addStatesVisitedAmount(self):
        self.statesVisitedAmount+=1

    def __getNextPos(self,tuple,dir):
        if(dir==Move.UPDiag):
            return (tuple[0]-1,tuple[1]+1);
        elif(dir==Move.LEFT):
            return (tuple[0]-1,tuple[1]);
        elif(dir==Move.DOWNDiag):
            return (tuple[0]-1,tuple[1]-1);
    
    def __is_inside(self,state):
        if state[0] < self.env.size and state[0]>-1 and state[1] < self.env.size and state[1]>-1:
            return True
        return False
    
    def __checkQueen(self,state):
        checkedNum = 0
        hashTable = {}
        moveArr = {Move.UPDiag,Move.LEFT,Move.DOWNDiag}
        for i in range(0,len(state)):
            queenPos = (i,state[i]);
            hashTable[str(queenPos)] = (True,False);
            for move in moveArr: 
                checked = False
                nextPos = self.__getNextPos(queenPos,move)
                while self.__is_inside(nextPos) and checked == False:
                    if hashTable.get(str(nextPos)) == None: 
                        hashTable[str(nextPos)] = (False,False)
                    elif hashTable[str(nextPos)][0]==True:
                        if(hashTable[str(queenPos)][1]==False):
                            checkedNum += 1
                            hashTable[str(queenPos)] = (True,True)
                        if(hashTable[str(nextPos)][1] == False):
                            checkedNum += 1
                            hashTable[str(nextPos)] = (True,True)
                        checked == True
                    nextPos = self.__getNextPos(nextPos,move)
        return checkedNum
#----------------------------------------------------------------------#
    def __findNeighbor(self,state):
        bestState= (state[0].copy(),state[1]);
        for i in range(0,len(state[0])):
            for j in range(0,len(state[0])):
                if(state[0][i] != j):
                    Neightbor = state[0].copy()
                    Neightbor[i] = j
                    val = self.__checkQueen(Neightbor)
                    possibleState = (Neightbor,val)
                    if(bestState[1]>possibleState[1]):
                        bestState = possibleState
        return bestState

    def hill_climbing(self):
        initState = list(self.env.table)
        currentState = (initState,self.__checkQueen(initState))
        max = self.env.size*2
        while self.getStatesVisitedAmount() < max:
            nextState = self.__findNeighbor(currentState);
            if nextState[1] >= currentState[1]:
                return currentState
            currentState = nextState
            self.__addStatesVisitedAmount()
#------------------------------------------------------------------------#
    def __findRandomNeighbor(self,state):
        Neightbor = state[0].copy()
        i = randint(0,len(Neightbor)-1)
        j = randint(0,len(Neightbor)-1)
        Neightbor[i] = j
        val = self.__checkQueen(Neightbor)
        return (Neightbor,val)
    
    def __schedule(self,t):
        return 1/t

    def simmulated_annealing(self):
        initState = list(self.env.table)
        currentState = (initState,self.__checkQueen(initState))
        t = 0
        while True:
            t+=1
            T = self.__schedule(t)
            if(T<0.03):
                return currentState
            nextState = self.__findRandomNeighbor(currentState);
            E = nextState[1]-currentState[1] 
            if E<0:
                currentState = nextState
            else:
                p = pow(math.e,-E/T);
                np = math.trunc(10*(1-p))
                p = math.trunc(10*p)
                a=choices([True,False],(p,np))
                if(a[0]==True):
                   currentState = nextState
            self.__addStatesVisitedAmount()
#------------------------------------------------------------------------#
    def genetic_algorithm(self):
        state = None
        return state