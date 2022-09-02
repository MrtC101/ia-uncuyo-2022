from enum import IntEnum
from turtle import down

class Solution(IntEnum):
    BFS = 1
    UniformCost = 2
    DFS = 3

class Move(IntEnum):
    UP = 0
    DOWN = 1 
    LEFT = 2
    RIGHT = 3 