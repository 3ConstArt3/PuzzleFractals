from Turtle.Utility.Motion import *
from math import e

class Designer:

    """
    A class that is used, to construct
    the final fractal puzzle's side.

    ...

    Attributes
    ----------
    motion: Motion
        An object, used to move
        the turtle on the canvas.
    """

    """
    Constructor definition
    """
    def __init__(self):
        self.motion = Motion()

    """
    Function definition
    """
    def construct(self, sideLength: float, depth: int) -> None:

        """
        Constructs, the fractal
        puzzle's side.

        ...

        Parameters
        ----------
        sideLength: float
            A float, indicating the length
            of the puzzle's side.

        depth: int
            An integer, indicating the
            depth of recursion.
        """

        maxDepthExceeded = (depth == 0)
        if maxDepthExceeded: return

        sideLength /= e

        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.motion.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.motion.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
