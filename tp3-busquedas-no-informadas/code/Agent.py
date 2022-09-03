import treelib as t
import myQueue
from Solution import Move

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

    def __already_in_frontier(self,state,frontier):
        return frontier.searchWithHash(state)

    def __already_explored(self,state,exploredList):
        if exploredList.searchWithHash(state) != None:
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
    def __think(self,state,frontier,exploredNodes,Tree,cost): #implementa las acciones a seguir
        #Cada estado representa un par ordenado (x,y) que existe en la matriz de environment
        newStateList =[self.__up(state),self.__down(state),self.__left(state),self.__right(state)]
        for i in range(0,len(newStateList)):
            newState = newStateList[i]
            if self.__is_inside(newState) == True:
                if self.__is_obstacle(newState) == False:
                    if self.__already_explored(newState,exploredNodes) == False:
                        lessCost = False
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
                  
    def __createMovesList(self,T,GoalNode):
        movesList = [GoalNode]
        parentID = T.ancestor(GoalNode.identifier)
        while parentID != None:
            currNode = T.get_node(parentID) 
            movesList.insert(0,currNode)
            parentID = T.ancestor(currNode.identifier)
        return movesList

    def __exploringFrontier(self,Tree,frontier,explored):
        while frontier.size>0:
            node = frontier.get()
            treeNode = node.data
            if self.env.ground[treeNode.data[0]][treeNode.data[1]] == "><":
                #devolver la lista de movimientos
                return self.__createMovesList(Tree,treeNode)
            else:
                cost = node.priority
                self.__think(treeNode.data,frontier,explored,Tree,cost)
            explored.append(treeNode)
            self.__addStatesVisitedAmount()
            del node
        return "No Solution"

    def __startTreeAndFrontier(self,frontier):
        Initial_Pos = self.env.initPos
        T = t.Tree()
        T.create_node(tag="Initial_Pos",identifier=str(Initial_Pos),parent=None,data=Initial_Pos)
        #0 is priority 
        frontier.add(T.get_node(str(Initial_Pos)),0)
        return T

    def __getSolution(self,frontier):
        T = self.__startTreeAndFrontier(frontier)
        explored = myQueue.PythonList()
        solution = self.__exploringFrontier(T,frontier,explored)
        del frontier
        del explored
        del T
        return solution

    def solveByBFS(self):
        self.resetStateVisitedAmount()
        frontier = myQueue.Queue()
        return self.__getSolution(frontier)

    def solveByDFS(self):
        self.resetStateVisitedAmount()
        frontier = myQueue.Stack()
        return self.__getSolution(frontier)

    def solveByUniformCost(self):
        self.resetStateVisitedAmount()
        frontier = myQueue.priorityQueue()
        return self.__getSolution(frontier)
        
#print(str(explored.hashTable),end="\n\n\n")