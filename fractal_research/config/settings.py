from math import e
from dataclasses import dataclass, field
from fractal_research.core.geometry import Point2D


@dataclass(frozen=True, slots=True)
class CanvasConfig:
    """Configuration of the drawing canvas."""

    width: int = 1200
    height: int = 630
    title: str = "Puzzle Fractal"
    background_color: str = "white"


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
    """Parameters controlling the geometry of the Puzzle Fractal."""

    start_position: Point2D = field(
        default_factory=lambda: Point2D(
            x=-300.0,
            y=0.0,
        )
    )

    polygon_side_count: int = 7

    recursion_depth: int = 5
    side_length: float = 300.0

    scale_factor: float = e

    turn_angle_degrees: float = 120.0
    arc_angle_degrees: float = 180.0

    def __post_init__(self) -> None:
        if self.polygon_side_count < 3:
            raise ValueError(
                "polygon_side_count must be at least 3."
            )

        if self.recursion_depth < 0:
            raise ValueError(
                "recursion_depth must be greater than or equal to zero."
            )

        if self.side_length <= 0:
            raise ValueError(
                "side_length must be greater than zero."
            )

        if self.scale_factor <= 0:
            raise ValueError(
                "scale_factor must be greater than zero."
            )


@dataclass(frozen=True, slots=True)
class ApplicationConfig:
    """Complete configuration of a fractal experiment."""

    canvas: CanvasConfig = field(default_factory=CanvasConfig)
    turtle: TurtleConfig = field(default_factory=TurtleConfig)
    fractal: PuzzleFractalConfig = field(
        default_factory=PuzzleFractalConfig
    )