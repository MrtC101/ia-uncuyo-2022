from enum import IntEnum

from matplotlib.sankey import RIGHT

class Solution(IntEnum):
    BACKTRACKING = 1 
    FOWARDCHECK = 2

class Move(IntEnum):
    UPDiag = 0
    LEFT = 1
    DOWNDiag = 2
    RIGHT = 3