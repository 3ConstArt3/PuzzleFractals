from turtle import *

from pygame.math import Vector2
from enum import Enum

class Direction(Enum):

    Left = 0
    Right = 1

class Setup:

    """
    Constructor definition
    """
    def __init__(self):
        self.resolution = Vector2(1200, 630)

    """ 
    Function definition
    """
    @staticmethod
    def move_to(point: Vector2) -> None:

        penup()
        goto(point.x, point.y)
        pendown()

    @staticmethod
    def turn(direction: Direction, angle: float) -> None:

        turnLeft = (direction == Direction.Left)
        left(angle) if turnLeft else right(angle)