from turtle import *

from pygame.math import Vector2
from enum import Enum

class Direction(Enum):

    """
    An enumerable class that helps with
    the definition of the model's
    direction.
    """

    Left = 0
    Right = 1

class Motion:

    """
    A class that is used, to define
    the basic movements of the turtle
    model, such as moving to a single
    point or turning to a specified
    direction.
    """

    """
    Constructor definition
    """
    def __init__(self):
        pass

    """ 
    Function definition
    """
    @staticmethod
    def move_to(point: Vector2) -> None:

        """
        Moves the turtle model to a point,
        without leaving a trace on
        the canvas.

        ...

        Parameters
        ----------
        point: Vector2
            The point, where the turtle
            should move at.
        """

        penup()
        goto(point.x, point.y)
        pendown()

    @staticmethod
    def turn(direction: Direction, angle: float) -> None:

        """
        Turns the turtle model, to the
        specified direction and angle.

        ...

        Parameters
        ----------
        direction: Direction
            The direction of the turn.

        angle: float
            The angle of rotation.
        """

        turnLeft = (direction == Direction.Left)
        left(angle) if turnLeft else right(angle)
