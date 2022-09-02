import treelib as t
import myQueue
from Solution import Move

class Agent:
    #resive como parametro un objeto Environment
    def __init__(self,env):
        self.env = env 
        self.statesVisitedAmount = 0

    def getStatesVisitedAmount(self):
        return self.statesVisitedAmount

    def __addStatesVisitedAmount(self):
        self.statesVisitedAmount+=1

    def __up(self,state):
        newState = (state[0],state[1]+1)
        return newState

    def __down(self,state):
        newState = (state[0],state[1]-1)
        return newState

    def __left(self,state):
        newState = (state[0]-1,state[1])
        return newState

    def __right(self,state):
        newState = (state[0]+1,state[1])
        return newState

    #def perspective(self): #verifica el entorno
    def __already_in_frontier(self,state,frontier):
        if isinstance(frontier,myQueue.priorityQueue):
            return frontier.searchWithHash(state)
        currentNode = frontier.head
        if currentNode != None:
            while currentNode!=None:
                frontiered = currentNode.data.data
                if state == frontiered:
                    return currentNode
                currentNode=currentNode.nextNode
        return None

    def __already_explored(self,state,exploredList):
        for i in range(0,len(exploredList)):
            explored = exploredList[i].data
            if state == explored:
                return True
        return False

    def __is_obstacle(self,state):
        if self.env.ground[state[0]][state[1]]=="[]":
            return True
        return False

    def __is_inside(self,state):
        if state[1] < self.env.sizes[1] and state[1]>-1 and state[0] < self.env.sizes[0] and state[0]>-1:
            return True
        return False

    #se crean los hijos y añaden a la frontera según los movimientos posibles
    def think(self,state,frontier,exploredNodes,Tree,cost): #implementa las acciones a seguir
        #Cada estado representa un par ordenado (x,y) que existe en la matriz de environment
        newStateList =[self.__up(state),self.__down(state),self.__left(state),self.__right(state)]
        for i in range(0,len(newStateList)):
            newState = newStateList[i]
            if self.__is_inside(newState) == True:
                if self.__is_obstacle(newState) == False:
                    if self.__already_explored(newState,exploredNodes) == False:
                        lessCost = False
                        #agregar hashtable
                        frontierNode = None
                        frontierNode = self.__already_in_frontier(newState,frontier)
                        if isinstance(frontier,myQueue.priorityQueue) and frontierNode != None:
                                #verificar si newState Cost es < a cost en frontier
                                oldcost = frontierNode.priority
                                newcost = cost+1
                                if oldcost > newcost:
                                    lessCost=True
                                    Tree.remove_node(frontierNode.data.identifier)
                                    frontier.delete(frontierNode)
                        if (lessCost and isinstance(frontier,myQueue.priorityQueue)) or frontierNode == None:
                            #se crea el nodo y se agrega a la frontera y al arbol
                            Tree.create_node(tag=Move(i).name,identifier=str(newState),parent=str(state),data=newState)
                            frontier.add(Tree.get_node(str(newState)),cost+1)
                  
    def createMovesList(self,T,GoalNode):
        movesList = [GoalNode]
        parentID = T.ancestor(GoalNode.identifier)
        while parentID != None:
            currNode = T.get_node(parentID) 
            movesList.insert(0,currNode)
            parentID = T.ancestor(currNode.identifier)
        return movesList

    def exploringFrontier(self,Tree,frontier,explored):
        while frontier.size>0:
            #print(str(frontier.hashTable),end="\n\n\n")
            node = frontier.get()
            treeNode=node.data
            cost=node.priority
            if self.env.ground[treeNode.data[0]][treeNode.data[1]] == "><":
                #devolver la lista de movimientos
                return self.createMovesList(Tree,treeNode)
            else:
                self.think(treeNode.data,frontier,explored,Tree,cost)
            explored.append(treeNode)
            #Tree.show()
            #print(explored)
            self.__addStatesVisitedAmount()
        return "No Solution"

    def createTree(self,frontier):
        tree = t.Tree()
        location = self.env.initPos
        tree.create_node(tag="Initial_Pos",identifier=str(location),parent=None,data=location)
        frontier.add(tree.get_node(str(location)),0)
        return tree

    def solveByBFS(self):
        frontier = myQueue.Queue()
        T = self.createTree(frontier)
        return self.exploringFrontier(T,frontier,explored=[])

    def solveByDFS(self):
        frontier = myQueue.Stack()
        T = self.createTree(frontier)
        return self.exploringFrontier(T,frontier,explored=[])

    def solveByUniformCost(self):
        frontier = myQueue.priorityQueue()
        T = self.createTree(frontier)
        return self.exploringFrontier(T,frontier,explored=[])
