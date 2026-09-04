from dataclasses import dataclass

from fractal_research.core.drawing_commands import TurnDirection


@dataclass(frozen=True, slots=True)
class RecursiveSide:
    """Represents a recursive occurrence of the fractal side."""
    pass


@dataclass(frozen=True, slots=True)
class ForwardRule:
    """Represents a forward movement."""

    length_factor: float = 1.0


@dataclass(frozen=True, slots=True)
class TurnRule:
    """Represents a rotation."""

    direction: TurnDirection
    angle_degrees: float


@dataclass(frozen=True, slots=True)
class ArcRule:
    """Represents a circular arc."""

    radius_factor: float = 1.0
    angle_degrees: float = 180.0


SideRule = (
    RecursiveSide
    | ForwardRule
    | TurnRule
    | ArcRule
)


@dataclass(frozen=True, slots=True)
class SidePatternConfig:
    """Defines the production rule of a fractal side."""

    operations: tuple[SideRule, ...]


PUZZLE_SIDE_PATTERN = SidePatternConfig(
    operations=(
        RecursiveSide(),

        ForwardRule(),

        RecursiveSide(),

        TurnRule(
            direction=TurnDirection.RIGHT,
            angle_degrees=120.0,
        ),

        RecursiveSide(),

        ArcRule(
            radius_factor=1.0,
            angle_degrees=180.0,
        ),

        RecursiveSide(),

        TurnRule(
            direction=TurnDirection.RIGHT,
            angle_degrees=120.0,
        ),

        RecursiveSide(),

        ForwardRule(),

        RecursiveSide(),
    )
)