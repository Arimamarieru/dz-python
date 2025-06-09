from enum import Enum

class CellType(str, Enum):
    EMPTY = " "
    TREE = "T"
    RIVER = "≈"
    FIRE = "F"
    BURNT = "x"

class Direction(tuple, Enum):
    UP    = (0, -1)
    DOWN  = (0, 1)
    LEFT  = (-1, 0)
    RIGHT = (1, 0)

