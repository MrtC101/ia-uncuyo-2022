class Node:
    previousNode = None
    nextNode = None
    data = None
    priority = None

class Stack:
    head = None
    lastNode = None
    size = 0
            
    def add(self,item,priority):
        newNode = Node()
        newNode.data=item
        newNode.priority = priority
        if self.head == None:
            self.head = newNode
            self.lastNode = newNode
        else:
            self.head.previousNode = newNode
            newNode.nextNode = self.head
            self.head = newNode
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
            self.head.previousNode=None
            node.nextNode=None
        self.size-=1
        return node

class Queue:
    head = None
    lastNode = None
    size = 0
            
    def add(self,item,priority):
        newNode = Node()
        newNode.data=item
        newNode.priority = priority
        if self.head == None:
            self.head = newNode
            self.lastNode = newNode
        else:
            self.head.previousNode = newNode
            newNode.nextNode = self.head
            self.head = newNode
        self.size+=1

    def get(self):
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
        return node

class priorityQueue:
    head = None
    lastNode = None
    size = 0

    def __init__(self):
        self.hashTable={}

    def add(self,item,priority):
        newNode = Node()
        newNode.data=item
        newNode.priority = priority
        self.hashTable[str(item.data)]=newNode
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
        return self.size
    
    def searchWithHash(self,data):
        try:
            r = self.hashTable[str(data)]
            return r
        except Exception:
            return None