from re import X
import treelib as t
from random import randint,choices, random
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
            if nextState[1] >= currentState[1]:#limite
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
    
    def __schedule(self,stateVistitedAmount,stateScore):
        return stateScore/stateVistitedAmount()

    def simulated_annealing(self):
        initState = list(self.env.table)
        currentState = (initState,self.__checkQueen(initState))
        while True:
            self.__addStatesVisitedAmount()
            T = self.__schedule(self.getStatesVisitedAmount,currentState[1])
            if(T < 0.03):#limite
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
#------------------------------------------------------------------------#
    def random_selection(self,population):
        i = randint(0,(len(population)-1))
        state = population[i] 
        return state

    def reproduce(self,x,y):
        newtable = []
        v = randint(0,len(x)-1)
        for i in range(0,len(x[0])):
            if(i<v):
                newtable.append(x[0][i])
            else:
                newtable.append(y[0][i])
        child = (newtable,self.__checkQueen(newtable))
        return child

    def mutate(self,state):
        posX = randint(0,len(state)-1)
        posY = randint(0,len(state)-1)
        newtable = state[0]
        newtable[posX] = posY
        newstate = (newtable,self.__checkQueen(newtable))
        return newstate

    def generatePopulation(self,populationSize,problemSize):
        population = []
        for i in range(0,populationSize):
            state = []
            for j in range(0,problemSize):
                state.append(randint(0,problemSize-1))
            population.append((state,self.__checkQueen(state)))
        return population

    def genetic_algorithm(self):
        popSize = self.env.size
        population = self.generatePopulation(popSize,self.env.size)
        limit = popSize * 10 #limite
        bestState = population[0]
        while(bestState[1] > 0 and self.getStatesVisitedAmount() < limit):
            new_population = []
            for i in range(0,len(population)):
                x = self.random_selection(population)
                y = self.random_selection(population)
                child = self.reproduce(x,y)
                if(choices([True,False],(0.1,0.9))[0]):
                    child = self.mutate(child);
                if(bestState[1]>child[1]):
                    bestState=child
                new_population.append(child)
            population = new_population
            self.__addStatesVisitedAmount()
        return bestState