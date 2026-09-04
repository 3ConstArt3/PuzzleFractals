from dataclasses import dataclass
from typing import TypeAlias

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

    radius_factor: float
    angle_degrees: float


SideRule: TypeAlias = (
    RecursiveSide
    | ForwardRule
    | TurnRule
    | ArcRule
)


@dataclass(frozen=True, slots=True)
class SidePatternConfig:
    """Defines the production rule of one fractal side."""

    operations: tuple[SideRule, ...]