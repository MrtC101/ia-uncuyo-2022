from enum import IntEnum

class Solution(IntEnum):
    BFS = 1
    UniformCost = 2
    DFS = 3
    DFSLimited = 4
    SameEnvironment = 5
    RandomEnvironment = 6

class Move(IntEnum):
    UP = 0
    DOWN = 1 
    LEFT = 2
    RIGHT = 3 

class Option(IntEnum):
    WhithGraphics = 1
    NoGraphics = 2