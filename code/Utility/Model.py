from Turtle.Utility.Designer import *

class Model:

    """
    A class that is used, to create
    the final fractal puzzle picture
    on the canvas.

    ...

    Attributes
    ----------
    designer: Designer
        An object, used to create
        the final puzzle object.

    start: Vector2
        A vector, indicating the
        starting position of the
        model.

    sideLength: float
        A number, that shows the
        length of the fractal
        puzzle's side.
    """

    """
    Constructor definition
    """
    def __init__(self, resolution: Vector2):

        self.designer = Designer()

        # A factor that determines the
        # percentage length of the fractal
        # puzzle's side.
        lengthFactor = 0.42

        # These parameters are used to
        # specify the exact starting
        # position of the turtle.
        factorX = -1 / 15
        factorY = 1 / 15

        startX = resolution.x * factorX
        startY = resolution.y * factorY
        self.start = Vector2(startX, startY)
        self.sideLength = lengthFactor * resolution.y

    """
    Function definition
    """
    def create(self) -> None:

        """
        A function that constructs the
        fractal puzzle, based on the idea
        of a regular n-polygon.
        """

        # This 18-colored palette, defines the
        # color range of the final puzzle shape.
        palette = [
            "#ff9aa2", "#ffb7b2", "#ffdac1",
            "#e2f0cb", "#b5ead7", "#c7ceea",
            "#1baaa0", "#7dddf5", "#fbc396",
            "#fc7e8a", "#aea0e8", "#d9ae9d",
            "#79d2b8", "#72c2e2", "#ffd275",
            "#fc91ad", "#b6c1ff", "#9a745f"
        ]

        # The depth, indicates the number of
        # iterations the model is going to make,
        # to create the puzzle fractal's side.
        depth, sides = 5, 6
        theta = 360 / sides
        for k in range(sides):

            index = k % sides
            pencolor(palette[index])

            self.designer.construct(self.sideLength, depth)
            self.designer.motion.turn(Direction.Right, theta)
