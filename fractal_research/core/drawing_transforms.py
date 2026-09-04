from collections.abc import Iterable, Iterator

from fractal_research.core.drawing_commands import (
    Arc,
    DrawingCommand,
    Forward,
    Turn,
)


def scale_commands(
    commands: Iterable[DrawingCommand],
    scale_factor: float,
) -> Iterator[DrawingCommand]:
    """Scales all distance-based drawing commands."""

    for command in commands:

        match command:

            case Forward(distance):
                yield Forward(
                    distance=distance * scale_factor
                )

            case Arc(radius, angle_degrees):
                yield Arc(
                    radius=radius * scale_factor,
                    angle_degrees=angle_degrees,
                )

            case Turn():
                yield command