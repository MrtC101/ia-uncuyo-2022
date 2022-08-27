from Environment import *
from Agent import *
from AgentAleatorio import *
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
            action = self.agent.think(state)
            if(action=="suck"):
                self.agent.points+=1
            self.time-=1

    def runWithGraphic(self):
        while(self.time > 0 and self.env.is_dirty() == True):
            self.env.print_enviroment()
            state = self.agent.perspective()
            action = self.agent.think(state)
            #self.env.accept_action(action)
            if(action=="suck"):
                self.agent.points+=1
            self.time-=1

    def get_Performance(self):
        return [1000-self.time,self.agent.points,self.env.total_dirt]
