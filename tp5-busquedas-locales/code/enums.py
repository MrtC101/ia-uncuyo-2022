from enum import IntEnum

class Solution(IntEnum):
    HILL_CLIMBING = 1 
    SIM_ANNEALING = 2
    GENETIC = 3

class Move(IntEnum):
    UPDiag = 0
    LEFT = 1
    DOWNDiag = 2