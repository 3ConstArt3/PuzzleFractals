from math import e
from dataclasses import dataclass, field

from fractal_research.fractals.puzzle.side_pattern import (
    PUZZLE_SIDE_PATTERN,
    SidePatternConfig,
)


@dataclass(frozen=True, slots=True)
class CanvasConfig:
    """Configuration of the drawing canvas."""

    width: int = 1200
    height: int = 630

    padding: float = 40.0

    title: str = "Puzzle Fractal"
    background_color: str = "white"

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError(
                "Canvas width must be greater than zero."
            )

        if self.height <= 0:
            raise ValueError(
                "Canvas height must be greater than zero."
            )

        if self.padding < 0:
            raise ValueError(
                "Canvas padding cannot be negative."
            )

        if 2 * self.padding >= self.width:
            raise ValueError(
                "Canvas padding is too large for its width."
            )

        if 2 * self.padding >= self.height:
            raise ValueError(
                "Canvas padding is too large for its height."
            )


@dataclass(frozen=True, slots=True)
class TurtleConfig:
    """Configuration of the Turtle drawing engine."""

    speed: int = 0
    delay: int = 0
    pen_size: int = 1
    hide_cursor: bool = True
    use_animation: bool = False


@dataclass(frozen=True, slots=True)
class PuzzleFractalConfig:

    polygon_side_count: int = 4
    recursion_depth: int = 5
    base_side_length: float = 400.0
    scale_factor: float = e

    side_pattern: SidePatternConfig = PUZZLE_SIDE_PATTERN


@dataclass(frozen=True, slots=True)
class ApplicationConfig:
    """Complete configuration of a fractal experiment."""

    canvas: CanvasConfig = field(default_factory=CanvasConfig)
    turtle: TurtleConfig = field(default_factory=TurtleConfig)
    fractal: PuzzleFractalConfig = field(
        default_factory=PuzzleFractalConfig
    )