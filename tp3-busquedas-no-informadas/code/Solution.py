from enum import IntEnum

class Solution(IntEnum):
    BFS = 1
    UniformCost = 2
    DFS = 3
    SameEnvironment = 4
    RandomEnvironment = 5

class Move(IntEnum):
    UP = 0
    DOWN = 1 
    LEFT = 2
    RIGHT = 3 

class Option(IntEnum):
    WhithGraphics = 1
    NoGraphics = 2