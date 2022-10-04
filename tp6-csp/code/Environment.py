from math import trunc
import random
class Environment:

    def __init__(self,size):
        self.size = size
        self.table = []
        self.domain = []
        for i in range(0,size):
            self.table.append(0)
        for i in range(0,size):
            currDomain = []
            for j in range(0,size):
                currDomain.append(j)
            self.domain.append(currDomain)
        
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

    def print_enviromentExtern(table):
        size = len(table)
        for i in range (size-1,-1,-1):
            for j in range (0,size):
                if(table[j]==i):
                    print("|<>",end="")
                else:
                    print("|  ",end="")
            print("|")
                