from math import trunc
from AgentLocation import *
import random
class Environment:

    def __init__(self,sizeX,sizeY,initPosX,initPosY,dirt_rate):
        self.total_dirt = trunc(sizeX*sizeY*dirt_rate)
        self.ground = self.__createMatrix(sizeX,sizeY)
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.agentPos = AgentLocation(initPosX,initPosY)
        self.__get_dirty()

    def __createMatrix(self,sizeX,sizeY):
        matrix = []
        for i in range(0,sizeY):
            matrix.append([" "]*sizeX)
        return matrix

    def __get_dirty(self):
        for i in range(self.total_dirt):
            while True:
                x = random.randint(0,self.sizeX-1)
                y = random.randint(0,self.sizeY-1)
                if  self.ground[y][x] == " ":
                    self.ground[y][x] = "x" 
                    break 

    def get_clean(self,agent,x,y):
        if self.ground[y][x] == "x":
            self.total_dirt -= 1
            self.ground[y][x]=" "
            agent.points+=1
            
        
    #no entiendo para que se usa  
    #def accept_action(self,action):
        
    def is_dirty(self):
        if self.total_dirt == 0:
            return False
        else: 
            return True
    
    #Implementado en la simulación
    #def get_performance(self):

    def print_enviroment(self):
        for i in range (0,self.sizeY):
            for j in range (0,self.sizeX):
                if not(i==self.agentPos.getY() and j== self.agentPos.getX()):
                    print("|"+self.ground[i][j],end="")
                else:
                    print("|O",end="")
            print("|")
        print()
        print("====================================")
                