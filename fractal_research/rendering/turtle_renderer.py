import turtle
from collections.abc import Iterable

from fractal_research.config.settings import (
    CanvasConfig,
    TurtleConfig,
)
from fractal_research.core.drawing_commands import (
    Arc,
    DrawingCommand,
    Forward,
    Turn,
    TurnDirection,
)
from fractal_research.core.geometry import Point2D
from fractal_research.rendering.renderer import Renderer


class TurtleRenderer(Renderer):
    """Renders fractal geometry using Python Turtle."""

    def __init__(
        self,
        canvas_config: CanvasConfig,
        turtle_config: TurtleConfig,
    ):
        self.canvas_config = canvas_config
        self.turtle_config = turtle_config

    def configure(self) -> None:
        """Configures the Turtle graphics environment."""

        turtle.title(self.canvas_config.title)
        turtle.bgcolor(
            self.canvas_config.background_color
        )

        turtle.setup(
            width=self.canvas_config.width,
            height=self.canvas_config.height,
        )

        turtle.delay(self.turtle_config.delay)
        turtle.speed(self.turtle_config.speed)

        turtle.tracer(
            1 if self.turtle_config.use_animation else 0
        )

        if self.turtle_config.hide_cursor:
            turtle.hideturtle()

        turtle.pensize(
            self.turtle_config.pen_size
        )

    def move_to(self, point: Point2D) -> None:
        """Moves the Turtle without drawing."""

        turtle.penup()
        turtle.goto(point.x, point.y)
        turtle.pendown()

    def render(
        self,
        commands: Iterable[DrawingCommand],
    ) -> None:
        """Executes the generated drawing commands."""

        for command in commands:
            self._execute(command)

    @staticmethod
    def _execute(command: DrawingCommand) -> None:
        """Executes a single drawing command."""

        match command:

            case Forward(distance):
                turtle.forward(distance)

            case Turn(direction, angle_degrees):
                if direction is TurnDirection.LEFT:
                    turtle.left(angle_degrees)
                else:
                    turtle.right(angle_degrees)

            case Arc(radius, angle_degrees):
                turtle.circle(
                    radius,
                    angle_degrees,
                )

    def finish(self) -> None:
        """Keeps the Turtle window open until clicked."""

        turtle.exitonclick()