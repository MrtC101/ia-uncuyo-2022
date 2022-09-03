class Node:
    previousNode = None
    nextNode = None
    data = None
    priority = 0

    def __init__(self,*args):
        """
        :param data: First param used from data
        :param priority: Second param and not nesesari used for priority queueu
        """
        if len(args)== 1:
            self.data = args[0]
        elif len(args) == 2:
            self.data = args[0]
            self.priority = args[1]
    """
    def __init__(self,data):
        self.data = data

    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

    """    
    def __del__(self):
        None

class List:
    head = None
    lastNode = None
    size = 0

    def __init__(self):
        self.hashTable={}
    
    def __del__(self):
        None

    def searchWithHash(self,data):
        """
        Search data on List in an internal hashtable.
        """
        try:
            return self.hashTable[str(data)] 
        except Exception:
            return None

    def add(self,item,priority=0):
        """
        Add the item to the List or Queue.
        :param priority: Is not need, and don't matter when adding items to the List.
        """
        newNode = Node(item)
        self.hashTable[str(item.data)] = newNode
        if self.head == None:
            self.head = newNode
            self.lastNode = newNode
        else:
            self.head.previousNode = newNode
            newNode.nextNode = self.head
            self.head = newNode
        self.size+=1
        return self.size

class Stack(List):

    def __init__(self):
        super().__init__()

    def __del__(self):
        None

    def get(self):
        """
        Returns the Last item added.
        """
        if self.head==None:
            return None
        node = self.head
        if self.head == self.lastNode:
            self.head=None
            self.lastNode=None
        else:
            self.head = node.nextNode
            self.head.previousNode=None
            node.nextNode=None
        self.size-=1
        del self.hashTable[str(node.data.data)]
        return node

class Queue(List):

    def __init__(self):
        super().__init__()

    def __del__(self):
        None

    def get(self):
        """
        Returns the First item added.
        """
        if self.head==None:
            return None
        node = self.lastNode
        if self.lastNode == self.head:
            self.head=None
            self.lastNode=None
        else:
            self.lastNode = node.previousNode
            self.lastNode.nextNode = None
            node.previousNode = None
        self.size-=1
        del self.hashTable[str(node.data.data)]
        return node

class priorityQueue(List):

    def __init__(self):
        super().__init__()
        
    def __del__(self):
        None

    #Override
    def add(self,item,priority):
        """
        Add an item to a Queue with priority.
        """
        newNode = Node(item,priority)
        self.hashTable[str(item.data)] = newNode
        if self.head == None:
            self.head = newNode
            self.lastNode = newNode
        else:
            if self.lastNode.priority <= newNode.priority:
                self.lastNode.nextNode=newNode
                newNode.previousNode=self.lastNode
                self.lastNode=newNode
            elif self.head.priority >= newNode.priority:
                self.head.previousNode = newNode
                newNode.nextNode = self.head
                self.head = newNode
            else:
                if ((self.head.priority+self.lastNode.priority)/2 >= newNode.priority):
                    currentNode=self.head
                    while not(currentNode.priority<newNode.priority and currentNode.nextNode.priority >= newNode.priority):
                        currentNode=currentNode.nextNode
                    currentNode.nextNode.previousNode = newNode
                    newNode.nextNode=currentNode.nextNode
                    currentNode.nextNode=newNode
                    newNode.previousNode=currentNode
                else:
                    currentNode=self.lastNode
                    while not(currentNode.priority > newNode.priority and currentNode.previousNode.priority <= newNode.priority):
                        currentNode=currentNode.previousNode
                    currentNode.previousNode.nextNode = newNode
                    newNode.previousNode=currentNode.previousNode
                    currentNode.previousNode=newNode
                    newNode.nextNode=currentNode
        self.size+=1
        return self.size

    def get(self):
        if self.head==None:
            return None
        node = self.head
        if self.head == self.lastNode:
            self.head=None
            self.lastNode=None
        else:
            self.head = node.nextNode
            node.nextNode=None
            self.head.previousNode=None
        self.size-=1
        del self.hashTable[str(node.data.data)]
        return node
    
    def delete(self,node):
        """
        Deletes the given Node.
        """
        if node == self.head:
            self.head = node.nextNode
            node.nextNode.previousNode = None
            node.nextNode = None
        elif node == self.lastNode:
            self.lastNode = node.previousNode
            node.previousNode.nextNode=None
            node.previousNode = None
        else:
            prevNode = node.previousNode
            prevNode.nextNode = node.nextNode
            node.nextNode.previousNode = prevNode
            node.nextNode = None
            node.previousNode=None
        self.size-=1
        del self.hashTable[str(node.data.data)]
        del node
        return self.size
    

class PythonList:

    def __init__(self):
        self.list = []
        self.hashTable={}
    
    def __del__(self):
        None

    def append(self,TreeNode):
        self.list.append(TreeNode)
        self.hashTable[str(TreeNode.data)] = len(self.list)-1
    
    def searchWithHash(self,data):
        try:
            return self.list[self.hashTable[str(data)]] 
        except Exception:
            return None