from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Point2D:
    """Represents a point in a two-dimensional coordinate system."""

    x: float
    y: float


@dataclass(frozen=True, slots=True)
class BoundingBox:
    """Represents the rectangular bounds of a generated path."""

    min_x: float
    min_y: float
    max_x: float
    max_y: float

    @property
    def width(self) -> float:
        return self.max_x - self.min_x

    @property
    def height(self) -> float:
        return self.max_y - self.min_y

    @property
    def center(self) -> Point2D:
        return Point2D(
            x=(self.min_x + self.max_x) / 2,
            y=(self.min_y + self.max_y) / 2,
        )