from Turtle.Utility.PuzzleFractal.Piece import *

class Model:

    """
    Constructor definition
    """
    def __init__(self):

        self.piece = Piece()
        self.screenWidth, self.screenHeight = self.piece.default.resolution

        lengthFactor = 0.42
        factorX = -1 / 12
        factorY = -1 / 12

        startX = self.screenWidth * factorX
        startY = self.screenHeight * factorY
        self.start = Vector2(startX, startY)
        self.sideLength = lengthFactor * self.screenHeight

    """
    Function definition
    """
    def create(self) -> None:

        palette = [
            "#ff9aa2", "#ffb7b2", "#ffdac1",
            "#e2f0cb", "#b5ead7", "#c7ceea",
            "#1baaa0", "#7dddf5", "#fbc396",
            "#fc7e8a", "#aea0e8", "#d9ae9d",
            "#79d2b8", "#72c2e2", "#ffd275",
            "#fc91ad", "#b6c1ff", "#9a745f"
        ]

        depth, sides = 5, 6
        theta = 360 / sides
        for k in range(sides):

            index = k % sides
            pencolor(palette[index])

            self.piece.construct(self.sideLength, depth)
            self.piece.default.turn(Direction.Right, theta)