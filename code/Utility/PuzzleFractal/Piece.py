from Turtle.Utility.Setup import *
from math import e

class Piece:

    """
    Constructor definition
    """
    def __init__(self):
        self.default = Setup()

    """
    Function definition
    """
    def construct(self, sideLength, depth):

        maxDepthExceeded = (depth == 0)
        if maxDepthExceeded: return

        sideLength /= e

        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)

    """
    Piece configurations:

    [0.12 * self.screenHeight, 3-4] => 
    /*
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        forward(sideLength)
     */        

    [0.33 * self.screenHeight, 3-4] => 
    /*
        forward(sideLength)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        forward(sideLength)
     */   

    [0.54 * self.screenHeight, 3-4-5] => 
    /*
        forward(sideLength)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        forward(sideLength)
     */        

    [0.66 * self.screenHeight, 3-4-5] => 
    /*
        forward(sideLength)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        forward(sideLength)
     */        

    [0.3 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.24 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.18 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.09 * self.screenHeight, 4] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.15 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.12 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.1 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.3 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.15 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.3 * self.screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
     */        

    [0.33 * screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 150 | 180 | 240)
     */        

    [0.21 * screenHeight, 4] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 150 | 180 | 240)
     */        

    [0.42 * screenHeight, 4] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 150 | 180 | 240)
     */        

    [0.24 * screenHeight, 4] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 150 | 180 | 240)
     */        

    [0.24 * screenHeight, 4] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
     */

    [0.66 * screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
     */

    [0.6 * screenHeight, 3] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
     */

    [0.48 * screenHeight, 4] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
     */

    [0.33 * screenHeight, 4] => 
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
     */

    [0.42 * screenHeight, 4] =>
    /*
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 90 | 120 | 180 | 240)
     */ 

    [0.33 * screenHeight, 4] =>
    /*
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
     */ 

    [0.54 * screenHeight, 4] =>
    /*
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
     */ 

    [0.6 * screenHeight, 4] =>
    /*
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
     */ 

    [0.33 * screenHeight, 3] =>
    /*
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)    
    */

    [0.81 * screenHeight, 4] =>
    /*
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)    
    */

    [0.42 * screenHeight, 4] =>
    /*
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 45 | 60 | 90 | 120 | 180)
    */

    [0.2 * screenHeight, 4] =>
    /*    
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
    */

    [0.16 * screenHeight, 4] =>
    /*
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
    */

    [0.42 * screenHeight, 4] =>
    /*    
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength | 180)
        self.construct(sideLength | 2 * sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength | 2 * sideLength, depth - 1)
        circle(sideLength | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)    
    */

    [0.39 * screenHeight, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength)
        self.default.turn(Direction.Left | Right, 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90 | 120 | 180 | 240)
        circle(sideLength)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)         
    */

    [0.3 * screenHeight, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength)
        self.default.turn(Direction.Left | Right, 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90 | 120 | 180 | 240)
        circle(sideLength)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
    */

    [390, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        circle(sideLength)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)    
    */

    [210, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
    */

    [240, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
    */

    [99, 4] =>
    /*
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
    */

    [180, 4] =>
    /*
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength | 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        forward(sideLength | 180)
        self.construct(sideLength, depth - 1)
    */

    [270, 4] =>
    /*
        circle(sideLength | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180)
        forward(sideLength)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        forward(sideLength)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength | 180)
    */

    [300, 4] =>
    /*
        circle(sideLength | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180)
        forward(sideLength)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 180 | 240)
        forward(sideLength)
        self.default.turn(Direction.Left, 30 | 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength | 180)
    */

    [150, 4] =>
    /*
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 90 | 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90 | 120)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
    */

    [150, 3] =>
    /*
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 90 | 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90 | 120)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
    */

    [120, 4] =>
    /*
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right | Left, 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 90 | 120 | 180 | 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
    */

    [300, 4] =>
    /*    
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength | 180)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right | Left, 90 | 120 | 180 | 210)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 90 | 120 | 180 | 210)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength | 180)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
    */

    [48, 4] =>
    /*
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
    */

    [120, 4] =>
    /*
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        circle(sideLength)  
    */

    [240, 4] =>
    /*
        forward(sideLength)
        circle(sideLength)
        self.default.turn(Direction.Right, 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120 | 180 | 240)
        circle(sideLength | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength | 180)
        self.default.turn(Direction.Left, 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120)
        circle(sideLength)
        forward(sideLength)
    */

    [180, 4] =>
    /*
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength | 180)
        self.default.turn(Direction.Right, 90 | 120 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90 | 120 | 180 | 210 | 240)
        circle(sideLength | 180)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
    */

    [330, 5] =>
    /*
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        circle(sideLength)
        forward(sideLength)
        self.construct(sideLength, depth - 1)  
    */

    [330, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 120)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)    
    */

    [180, 3] =>
    /*
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 240)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Left, 240)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
    */

    [200, 3] =>
    /*
        circle(sideLength)
        self.default.turn(Direction.Left, 120)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 60)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 60)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120)
        circle(sideLength)
    */

    [240, 4] =>
    /*
        self.default.turn(Direction.Left, 120)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 60)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 60)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 240)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Left, 120)
    */

    [180,4 ] =>
    /*
        self.default.turn(Direction.Left, 120)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 240)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Left, 120)
    */

    [210, 3] =>
    /*
        self.default.turn(Direction.Left, 120)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 240)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Left, 120)
    */

    [81, 4] =>
    /*
        self.default.turn(Direction.Right | Left, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Left | Right, 90 | 60)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90 | 60)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 120)
    */

    [180, 4] =>
    /*
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Right, 180)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 180)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
    */

    [180, 5] =>
    /*
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
    */

    [300, 5] =>
    /*
        self.default.turn(Direction.Left, 180)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.default.turn(Direction.Left, 180)
    */

    [210, 5] =>
    /*
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 90 | 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90 | 180)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
    */

    [160, 5] =>
    /*
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
    */

    [240, 4] =>
    /*
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
    */

    [240, 4] =>
    /*
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
    */

    [330, 4] =>
    /*
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
    */

    [200, 3] =>
    /*
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
    */

    [180, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
    */

    [180, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength)
        self.construct(sideLength, depth - 1)
    */

    [123, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
    /*

    [600, 3] =>
    /*
        self.default.turn(Direction.Left | Right, 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 120 | 180 | 240)
    */

    [3600, 4] =>
    /*
        self.default.turn(Direction.Right | Left, 120 | 150 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 120 | 150 | 180 | 210)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 120 | 150 | 180 | 210)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 120 | 150 | 180 | 210 | 240)
    */

    [150, 3] =>
    /*
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 60 | 90 | 120 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 60 | 90 | 120 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 180 | 210 | 240)
    */

    [1500, 4] =>
    /*
        self.default.turn(Direction.Left | Right, 60 | 75 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 75 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 75 | 90 | 120 | 150 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 60 | 75 | 90 | 120 | 150 | 180 | 240)
    */

    [810, 4] =>
    /*
        self.default.turn(Direction.Left | Right, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 60 | 90 | 120 | 180 | 240)
    */

    [540, 4] =>
    /*
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 | 60 | 90 | 120 | 180 | 210 | 240)
    */

    [1100, 3] =>
    /*
        self.default.turn(Direction.Left | Right, 90 | 120 | 150 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90 | 120 | 150 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120 | 150 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90 | 120 | 150 | 180 | 210 | 240)
    */

    [420, 5] =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 210)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 210)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
    */

    [480, 3] => 
    /*
        When depth == 0, change the forward(sideLength) --> circle(sideLength, 180)
        for more beautiful shapes to be made :).

        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 150 | 180 | 210 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 150 | 180 | 210 | 240)
    */

    [230, 3] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 * k (e) [1, 8])
        self.construct(sideLength, depth - 1)
    */

    [7200, 4] =>
    /*
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
    */

    [120, 5] =>
    /*
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 45 | 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 45 | 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 90 | 120 | 180 | 240)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
    */

    [300, 5] =>
    /*
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 150)
        self.default.turn(Direction.Right, 150)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
    */

    [600, 5] =>
    /*
        self.default.turn(Direction.Left | Right, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 210)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 21 | 30 | 60 | 90 | 120 | 150 | 180 | 210)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 21 | 30 | 60 | 90 | 120 | 150 | 180 | 210)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 30 | 60 | 90 | 120 | 150 | 180 | 210)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 180)
    */

    [2400, 6] =>
    /*
        self.default.turn(Direction.Right | Left, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 180)
    */

    [180, 5] =>
    /*
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
        circle(sideLength, 150)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 150)
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
        circle(sideLength, 180)
    */

    [240, 6] =>
    /*
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
        circle(sideLength, 180)
    */

    [180, 6] =>
    /*
        circle(sideLength, 180)
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
        circle(sideLength, 180)
    */

    [220, 6] =>
    /*
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
        circle(sideLength, 180)
    */

    [420, 6] =>
    /*
        forward(sideLength)
        self.default.turn(Direction.Left, 60)
        self.construct(sideLength, depth - 1)
        forward(sideLength/2)
        self.default.turn(Direction.Right, 90)
        forward(sideLength/2)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 60)
        forward(sideLength)
    */

    [200, 6] =>
    /*
        self.default.turn(Direction.Left, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 30 | 60 | 75 | 90)
        self.default.turn(Direction.Left, 60 | 120 | 150 | 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 180)
    */

    [300, 6 | 5] =>
    /*
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120 | 150 | 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 60 | 90 | 120 | 180)
    */

    [810, 6] =>
    /*
         self.default.turn(Direction.Left | Right, 180 | 90)
         self.construct(sideLength, depth - 1)
         circle(sideLength, 45 | 60 | 90 | 180)
         self.construct(sideLength, depth - 1)
         self.construct(sideLength, depth - 1)
         circle(sideLength, 45 | 60 | 90 | 180)
         self.construct(sideLength, depth - 1)
         self.default.turn(Direction.Left | Right, 180 | 90)
    */

    [120, 6] =>
    /*
        self.default.turn(Direction.Left | Right, 90)
        self.construct(sideLength, depth - 1)d
        circle(sideLength, 90 | 180 | 60)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180 | 60)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90)        
    */

    [810, 6] =>
    /*
         self.default.turn(Direction.Left, 90)
         self.construct(sideLength, depth - 1)
         self.default.turn(Direction.Right, 90)
         self.construct(sideLength, depth - 1)
         circle(sideLength, 60 | 90 | 180)
         self.construct(sideLength, depth - 1)
         self.default.turn(Direction.Right, 90)
         self.construct(sideLength, depth - 1)
         self.default.turn(Direction.Left, 90)
    */

    [1200, 6] =>
    /*
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 60)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
    */

    [120, 6] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120)
        circle(sideLength, 120)
        self.default.turn(Direction.Left, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 120)
        self.construct(sideLength, depth - 1)
    */

    [372, 5] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 120)
        self.construct(sideLength, depth - 1)
    */

    [120, 5] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 120)
        self.construct(sideLength, depth - 1)
    */

    [130, 6] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right | Left, 120)
        self.default.turn(Direction.Right | Left, 120)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
    */

    [150, 6] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 120)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
    */

    [270, 6] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.default.turn(Direction.Left, 120)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
    */

    [180, 6] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 120)
        self.default.turn(Direction.Right | Left, 120)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
    */

    [300, 6] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90 | 180)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120 | 60)
        # circle(sideLength, 90 | 180)
        self.default.turn(Direction.Right, 120 | 60)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90 | 180)
        self.construct(sideLength, depth - 1)
    */

    [240, 6] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60 | 90 | 120)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 60 | 90 | 120)
        self.construct(sideLength, depth - 1)
    */

    [180, 5] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 60)
        circle(sideLength, 180)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 180)
        self.default.turn(Direction.Right, 60)
        self.construct(sideLength, depth - 1)
    */

    [999, 5] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 120)
        self.construct(sideLength, depth - 1)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 120)
        self.construct(sideLength, depth - 1)
    */

    [390, 9] =>
    /*
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
    */

    [420, 6] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        circle(sideLength, 90)
        self.default.turn(Direction.Left, 90)
        circle(sideLength, 90)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
    */

    [250, 8] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        circle(sideLength, 90)
        circle(sideLength, 90)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
    */

    [270, 8] =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.default.turn(Direction.Left, 90)
        circle(2 * sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
    */

    [240, 9] => 
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        circle(2 * sideLength, 90)
        self.default.turn(Direction.Left | Right, 90)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
    */

    [300, 9] =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        circle(2 * sideLength, 90)
        self.default.turn(Direction.Left, 90)
        forward(2 * sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
    */

    [390, 7] =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        circle(2 * sideLength, 90)
        self.default.turn(Direction.Left, 90)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
    */        

    [11000, 8] =>
    /*
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
    */

    [12000, 8] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right | Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left | Right, 90)
    */    

    [33000, 8] =>
    /*
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
    */

    [42000, 9] =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
    */

    [720, 8] =>
    /*
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        bk(sideLength)
        self.default.turn(Direction.Left, 90)
    */

    [300, 3] =>
    /*
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        bk(sideLength)
        self.default.turn(Direction.Left, 90)
    */

    [480, 7], N = 13 =>
    /*
        self.default.turn(Direction.Left, 90)
        circle(sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
    */

    [540, 6], N = 8 =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        circle(sideLength, 90)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 90)
    */

    [1200, 8] =>
    /* 
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
    */

    [1200, 7] =>
    /* 
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
    */

    [2700, 5] =>
    /* 
        self.default.turn(Direction.Left, 90)
        self.construct(2 * sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(sideLength, depth - 1)
    */

    [810, 6] =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        self.construct(2 * sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
    */

    [240, 7] =>
    /*
        self.default.turn(Direction.Left, 90)
        circle(2*sideLength, 90)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Left, 90)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        forward(sideLength)
        self.default.turn(Direction.Right, 180)
        self.construct(sideLength, depth - 1)
    */

    [180, 6] =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        circle(2*sideLength, 90)
        self.default.turn(Direction.Left, 90)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 90)
        forward(sideLength)
        self.construct(sideLength, depth - 1)
        self.default.turn(Direction.Right, 180)
    */

    [300, 8] =>
    /*
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        circle(2*sideLength, 90)
        self.default.turn(Direction.Left, 90)
        self.construct(sideLength, depth - 1)
        forward(sideLength)
        self.default.turn(Direction.Right, 90)
    */
"""