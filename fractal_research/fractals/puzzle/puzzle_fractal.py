from collections.abc import Iterator

from fractal_research.config.settings import PuzzleFractalConfig
from fractal_research.core.drawing_commands import (
    DrawingCommand,
    Turn,
    TurnDirection,
)
from fractal_research.core.geometry import Point2D
from fractal_research.fractals.puzzle.side_generator import (
    PuzzleFractalSideGenerator,
)


class PuzzleFractal:
    """Generates a regular polygon composed of fractal sides."""

    def __init__(
        self,
        config: PuzzleFractalConfig,
    ):
        self.config = config

        self.side_generator = PuzzleFractalSideGenerator(
            config
        )

    @property
    def start_position(self) -> Point2D:
        """Returns the initial position of the fractal."""

        return self.config.start_position

    @property
    def polygon_exterior_angle_degrees(self) -> float:
        """Returns the exterior angle of the regular polygon."""

        return (
            360.0 / self.config.polygon_side_count
        )

    def generate(self) -> Iterator[DrawingCommand]:
        """Generates the complete polygonal Puzzle Fractal."""

        side_rotation = (
            self.side_generator.calculate_net_rotation(
                self.config.recursion_depth
            )
        )

        polygon_rotation = (
            self.polygon_exterior_angle_degrees
        )

        correction_rotation = (
            polygon_rotation - side_rotation
        )

        for _ in range(
            self.config.polygon_side_count
        ):
            yield from self.side_generator.generate_side(
                side_length=self.config.side_length,
                recursion_depth=self.config.recursion_depth,
            )

            yield self._create_turn(
                correction_rotation
            )

    @staticmethod
    def _create_turn(
        signed_angle_degrees: float,
    ) -> Turn:
        """Creates a turn from a signed rotation angle."""

        if signed_angle_degrees >= 0:
            return Turn(
                direction=TurnDirection.LEFT,
                angle_degrees=signed_angle_degrees,
            )

        return Turn(
            direction=TurnDirection.RIGHT,
            angle_degrees=abs(signed_angle_degrees),
        )