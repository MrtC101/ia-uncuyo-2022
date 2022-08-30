class AgentLocation:
    
    def __init__(self,x,y):
        self.X = x
        self.Y = y
    
    def setX(self,x):
        self.X = x
    
    def setY(self,y):
        self.Y = y
    
    def setXY(self,x,y):
        self.setX(x)
        self.setY(y)
    
    def getX(self):
        return self.X

    def getY(self):
        return self.Y