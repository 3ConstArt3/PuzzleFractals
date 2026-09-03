from collections.abc import Iterator

from fractal_research.config.settings import PuzzleFractalConfig
from fractal_research.core.drawing_commands import (
    Arc,
    DrawingCommand,
    Forward,
    Turn,
    TurnDirection,
)


class PuzzleFractalSideGenerator:
    """Generates the recursive geometry of one Puzzle Fractal side."""

    RECURSIVE_SUBSIDE_COUNT = 6

    def __init__(self, config: PuzzleFractalConfig):
        self.config = config

    def calculate_net_rotation(
            self,
            recursion_depth: int,
    ) -> float:
        """
        Calculates the net heading rotation produced
        by one complete fractal side.

        Positive values represent left turns.
        Negative values represent right turns.
        """

        rotation = 0.0

        local_rotation = (
                self.config.arc_angle_degrees
                - 2 * self.config.turn_angle_degrees
        )

        for _ in range(recursion_depth):
            rotation = (
                    self.RECURSIVE_SUBSIDE_COUNT * rotation
                    + local_rotation
            )

            rotation = self._normalize_angle(rotation)

        return rotation

    @staticmethod
    def _normalize_angle(angle_degrees: float) -> float:
        """Normalizes an angle to the interval [-180, 180)."""

        return (
                (angle_degrees + 180.0) % 360.0
        ) - 180.0

    def generate_side(
        self,
        side_length: float,
        recursion_depth: int,
    ) -> Iterator[DrawingCommand]:

        if recursion_depth == 0:
            return

        scaled_side_length = (
            side_length / self.config.scale_factor
        )

        yield from self.generate_side(
            scaled_side_length,
            recursion_depth - 1,
        )

        yield Forward(scaled_side_length)

        yield from self.generate_side(
            scaled_side_length,
            recursion_depth - 1,
        )

        yield Turn(
            direction=TurnDirection.RIGHT,
            angle_degrees=self.config.turn_angle_degrees,
        )

        yield from self.generate_side(
            scaled_side_length,
            recursion_depth - 1,
        )

        yield Arc(
            radius=scaled_side_length,
            angle_degrees=self.config.arc_angle_degrees,
        )

        yield from self.generate_side(
            scaled_side_length,
            recursion_depth - 1,
        )

        yield Turn(
            direction=TurnDirection.RIGHT,
            angle_degrees=self.config.turn_angle_degrees,
        )

        yield from self.generate_side(
            scaled_side_length,
            recursion_depth - 1,
        )

        yield Forward(scaled_side_length)

        yield from self.generate_side(
            scaled_side_length,
            recursion_depth - 1,
        )