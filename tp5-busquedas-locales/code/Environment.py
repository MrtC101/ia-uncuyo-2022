from math import trunc
import random
class Environment:

    def __init__(self,size):
        self.size = size
        self.table = []
        self.__generate_table()

    def __generate_table(self):
        for i in range(0,self.size):
            self.table.append(random.randint(0,self.size-1))

    def print_enviroment(self):
        for i in range (self.size-1,-1,-1):
            for j in range (0,self.size):
                if(self.table[j]==i):
                    print("|<>",end="")
                else:
                    print("|  ",end="")
            print("|")
        print()
        print("====================================")
                