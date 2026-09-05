from dataclasses import dataclass, field

from fractals.puzzle.side_pattern import (
    SidePatternConfig,
)


@dataclass(frozen=True, slots=True)
class CanvasConfig:

    width: int = 1200
    height: int = 630
    padding: float = 40.0

    title: str = "Puzzle Fractal"
    background_color: str = "white"


@dataclass(frozen=True, slots=True)
class TurtleConfig:

    speed: int = 0
    delay: int = 0
    pen_size: int = 1

    hide_cursor: bool = True
    use_animation: bool = False


@dataclass(frozen=True, slots=True)
class PuzzleFractalConfig:
    """Configuration of one Puzzle Fractal generation."""

    id: str

    side_count: int
    recursion_depth: int

    base_side_length: float
    scale_factor: float

    side_pattern: SidePatternConfig

    def __post_init__(self) -> None:

        if self.side_count < 3:
            raise ValueError(
                "side_count must be at least 3."
            )

        if self.recursion_depth < 0:
            raise ValueError(
                "recursion_depth cannot be negative."
            )

        if self.base_side_length <= 0:
            raise ValueError(
                "base_side_length must be greater than zero."
            )

        if self.scale_factor <= 0:
            raise ValueError(
                "scale_factor must be greater than zero."
            )

        if not self.side_pattern.operations:
            raise ValueError(
                "side_pattern must contain at least one operation."
            )


@dataclass(frozen=True, slots=True)
class ApplicationConfig:

    fractal: PuzzleFractalConfig

    canvas: CanvasConfig = field(
        default_factory=CanvasConfig
    )

    turtle: TurtleConfig = field(
        default_factory=TurtleConfig
    )