from math import trunc
import random
class Environment:

    def __init__(self,sizeX,sizeY,initPosX,initPosY,goalPosX,goalPosY,obstacles_rate):
        self.total_obstacles = trunc(sizeX*sizeY*obstacles_rate)
        self.ground = self.__createMatrix(sizeX,sizeY)
        self.sizes = (sizeX,sizeY)
        self.initPos = (initPosX ,initPosY)
        self.ground[initPosX][initPosY] = "<>"
        self.ground[goalPosX][goalPosY] = "><"
        self.__generate_obstacles()

    def __createMatrix(self,sizeX,sizeY):
        matrix = []
        for i in range(0,sizeY):
            matrix.append(["  "]*sizeX)
        return matrix

    def __generate_obstacles(self):
        for i in range(self.total_obstacles):
            while True:
                x = random.randint(0,self.sizes[0]-1)
                y = random.randint(0,self.sizes[1]-1)
                if  self.ground[y][x] == "  ":
                    self.ground[y][x] = "[]" 
                    break 
                
    #Implementado en la simulación
    #def get_performance(self):

    def print_enviroment(self):
        for i in range (0,self.sizes[1]):
            k=self.sizes[1]-1-i
            for j in range (0,self.sizes[0]):
                if not(k==self.initPos[1] and j== self.initPos[0]):
                    print("|"+self.ground[j][k],end="")
                else:
                    print("|<>",end="")
            print("|")
        print()
        print("====================================")
                