from Environment import *
from Agent import *
from AgentAleatorio import *
import time
import random

class Simulation:

    def __init__(self,size,dirt_rate,num):
        self.time=1000
        self.env = Environment(size,size,random.randint(0,size-1),random.randint(0,size-1),dirt_rate)
        if num == 1:
            self.agent = Agent(self.env)
        elif num == 2:
            self.agent = AgentAletorio(self.env)
    
    def run(self):
        while(self.time > 0 and self.env.is_dirty() == True):
            state = self.agent.perspective()
            self.agent.think(state)
            self.time-=1

    def runWithGraphic(self):
        while(self.time > 0 and self.env.is_dirty() == True):
            self.env.print_enviroment()
            time.sleep(0.25)
            state = self.agent.perspective()
            self.agent.think(state)
            self.time-=1

    def get_Performance(self):
        return [1000-self.time,self.agent.points,self.env.total_dirt]
