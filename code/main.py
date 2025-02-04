from Turtle.Utility.Model import *

class Solution:

    """
    A class that is used, to
    solve the problem, presented.

    ...

    Attributes
    ----------
    resolution: Vector2
        A vector, indicating the
        canvas' resolution.

    motion: Motion
        An object, used to move
        the turtle on the canvas.

    model: Model
        An object, used to create
        a turtle model, that will
        design the puzzle.
    """

    """
    Constructor definition
    """
    def __init__(self):

        self.resolution = Vector2(1200, 630)

        self.motion = Motion()
        self.model = Model(self.resolution)

    """ 
    Function definition
    """
    def setup_screen(self) -> None:

        """
        A function that sets up the basic
        attributes of a canvas, such as its
        title, resolution and background color.
        """

        title("Puzzle Fractal")
        bgcolor("black")
        setup(self.resolution.x, self.resolution.y)

    @staticmethod
    def modify_state() -> None:

        """
        A function that modifies the
        state of the turtle, such as
        its speed and its delay.
        """

        delay(0)
        speed(0)
        tracer(0)

        hideturtle()
        pensize(1)

    def solve(self) -> None:

        """
        The main function of the program,
        where all outputs are produced.
        """

        self.setup_screen()
        self.modify_state()

        self.motion.move_to(self.model.start)
        self.model.create()
        exitonclick()

if __name__ == "__main__":

    solution = Solution()
    solution.solve()
