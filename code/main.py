from Turtle.Utility.PuzzleFractal.Puzzle import *

class Solution:

    """
    Constructor definition
    """
    def __init__(self):

        self.default = Setup()
        self.model = Model()

    """ 
    Function definition
    """
    def setup_screen(self) -> None:

        title("Puzzle Fractal")
        bgcolor("black")

        resolution = self.default.resolution
        setup(resolution.x, resolution.y)

    @staticmethod
    def modify_state() -> None:

        delay(0)
        speed(0)
        tracer(0)

        hideturtle()
        pensize(1)

    def solve(self) -> None:

        self.setup_screen()
        self.modify_state()

        home()
        self.model.create()
        exitonclick()

if __name__ == "__main__":

    solution = Solution()
    solution.solve()
