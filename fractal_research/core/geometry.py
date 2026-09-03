from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Point2D:
    """Represents a point in a two-dimensional coordinate system."""

    x: float
    y: float


@dataclass(frozen=True, slots=True)
class CanvasSize:
    """Represents the dimensions of a drawing canvas."""

    width: int
    height: int