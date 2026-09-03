from dataclasses import dataclass
from enum import Enum, auto


class TurnDirection(Enum):
    """Defines the direction of a rotational movement."""

    LEFT = auto()
    RIGHT = auto()


@dataclass(frozen=True, slots=True)
class Forward:
    """Moves the drawing cursor forward."""

    distance: float


@dataclass(frozen=True, slots=True)
class Turn:
    """Rotates the drawing cursor."""

    direction: TurnDirection
    angle_degrees: float


@dataclass(frozen=True, slots=True)
class Arc:
    """Draws a circular arc."""

    radius: float
    angle_degrees: float


DrawingCommand = Forward | Turn | Arc