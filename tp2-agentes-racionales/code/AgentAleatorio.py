import random
class AgentAletorio:
    #resive como parametro un objeto Environment
    def __init__(self,env):
        self.env = env
        self.currPos = env.agentPos
        self.points = 0

    def up(self):
        self.currPos.setY(self.currPos.getY()+1)

    def down(self):
        self.currPos.setY(self.currPos.getY()-1)
    
    def left(self):
        self.currPos.setX(self.currPos.getX()-1)

    def right(self):
        self.currPos.setX(self.currPos.getX()+1)

    def suck(self):
        self.env.get_clean(self,self.currPos.getX(),self.currPos.getY())

    def idle(self):
        None

    def perspective(self): #verifica el entorno
        envirom =self.env
        if envirom.ground[self.currPos.getY()][self.currPos.getX()] == 'x':
            return "dirty"
        else:
            return "clean"
    
    def think(self,state): #implementa las acciones a seguir
        while True:
            num = random.randint(0,5)
            if(num==0 and self.currPos.getY()+1 < self.env.sizeY):
                self.up()
                return "up"
            elif(num==1 and self.currPos.getY()-1 > -1):
                self.down()
                return "down"
            elif(num==2 and self.currPos.getX()-1 > -1):
                self.left()
                return "left"
            elif(num==3 and self.currPos.getX()+1 < self.env.sizeX):
                self.right()
                return "right"
            elif(num==4):
                self.suck()
                return "suck"
            elif(num==5):
                self.idle()
                return "idle"

