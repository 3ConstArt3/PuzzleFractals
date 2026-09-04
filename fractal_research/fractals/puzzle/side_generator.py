from collections.abc import Iterator

from fractal_research.config.settings import PuzzleFractalConfig
from fractal_research.core.drawing_commands import (
    Arc,
    DrawingCommand,
    Forward,
    Turn,
    TurnDirection,
)
from fractal_research.fractals.puzzle.side_pattern import (
    ArcRule,
    ForwardRule,
    RecursiveSide,
    TurnRule,
)


class PuzzleFractalSideGenerator:
    """Generates one fractal side from a configurable production rule."""

    def __init__(
        self,
        config: PuzzleFractalConfig,
    ):
        self.config = config

    def generate_side(
        self,
        side_length: float,
        recursion_depth: int,
    ) -> Iterator[DrawingCommand]:
        """Generates one recursive fractal side."""

        if recursion_depth == 0:
            return

        scaled_side_length = (
            side_length / self.config.scale_factor
        )

        for operation in self.config.side_pattern.operations:

            match operation:

                case RecursiveSide():
                    yield from self.generate_side(
                        side_length=scaled_side_length,
                        recursion_depth=recursion_depth - 1,
                    )

                case ForwardRule(length_factor):
                    yield Forward(
                        distance=(
                            scaled_side_length
                            * length_factor
                        )
                    )

                case TurnRule(direction, angle_degrees):
                    yield Turn(
                        direction=direction,
                        angle_degrees=angle_degrees,
                    )

                case ArcRule(
                    radius_factor,
                    angle_degrees,
                ):
                    yield Arc(
                        radius=(
                            scaled_side_length
                            * radius_factor
                        ),
                        angle_degrees=angle_degrees,
                    )

    def calculate_net_rotation(
        self,
        recursion_depth: int,
    ) -> float:
        """
        Calculates the net heading rotation produced
        by one complete fractal side.
        """

        if recursion_depth == 0:
            return 0.0

        recursive_rotation = self.calculate_net_rotation(
            recursion_depth - 1
        )

        total_rotation = 0.0

        for operation in self.config.side_pattern.operations:

            match operation:

                case RecursiveSide():
                    total_rotation += recursive_rotation

                case ForwardRule():
                    pass

                case TurnRule(direction, angle_degrees):
                    if direction is TurnDirection.LEFT:
                        total_rotation += angle_degrees
                    else:
                        total_rotation -= angle_degrees

                case ArcRule(radius_factor, angle_degrees):
                    if radius_factor >= 0:
                        total_rotation += angle_degrees
                    else:
                        total_rotation -= angle_degrees

        return self._normalize_angle(
            total_rotation
        )

    @staticmethod
    def _normalize_angle(
        angle_degrees: float,
    ) -> float:
        """Normalizes an angle to [-180, 180)."""

        return (
            (angle_degrees + 180.0) % 360.0
        ) - 180.0