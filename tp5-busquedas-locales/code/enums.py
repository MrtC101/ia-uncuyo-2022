from enum import IntEnum

class Solution(IntEnum):
    HILL_CLIMBING = 1 
    SIMM_ANNEALING = 2
    GENETIC = 3
    RunAll = 4

class Move(IntEnum):
    UPDiag = 0
    LEFT = 1
    DOWNDiag = 2