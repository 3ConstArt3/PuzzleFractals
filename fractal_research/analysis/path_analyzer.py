import math
from collections.abc import Iterable

from fractal_research.core.drawing_commands import (
    Arc,
    DrawingCommand,
    Forward,
    Turn,
    TurnDirection,
)
from fractal_research.core.geometry import BoundingBox, Point2D


class PathAnalyzer:
    """Analyzes the geometry produced by drawing commands."""

    @staticmethod
    def _angle_is_on_arc(
            angle_degrees: float,
            start_degrees: float,
            extent_degrees: float,
    ) -> bool:

        if abs(extent_degrees) >= 360.0:
            return True

        angle = angle_degrees % 360.0
        start = start_degrees % 360.0

        if extent_degrees >= 0:

            difference = (angle - start) % 360.0
            return difference <= extent_degrees

        difference = (start - angle) % 360.0
        return difference <= abs(extent_degrees)

    def _analyze_arc(
            self,
            position: Point2D,
            heading_degrees: float,
            radius: float,
            extent_degrees: float,
    ) -> tuple[Point2D, float, BoundingBox]:

        heading_radians = math.radians(
            heading_degrees
        )

        center = Point2D(
            x=position.x
              - radius * math.sin(heading_radians),

            y=position.y
              + radius * math.cos(heading_radians),
        )

        start_angle = heading_degrees - 90.0
        end_angle = start_angle + extent_degrees

        candidate_angles = [
            start_angle,
            end_angle,
            0.0,
            90.0,
            180.0,
            270.0,
        ]

        points: list[Point2D] = []

        for angle in candidate_angles:

            if (
                    angle in (start_angle, end_angle)
                    or self._angle_is_on_arc(
                angle,
                start_angle,
                extent_degrees,
            )
            ):
                angle_radians = math.radians(angle)

                points.append(
                    Point2D(
                        x=center.x
                          + radius * math.cos(angle_radians),

                        y=center.y
                          + radius * math.sin(angle_radians),
                    )
                )

        end_angle_radians = math.radians(
            end_angle
        )

        end_position = Point2D(
            x=center.x
              + radius * math.cos(end_angle_radians),

            y=center.y
              + radius * math.sin(end_angle_radians),
        )

        bounds = BoundingBox(
            min_x=min(point.x for point in points),
            min_y=min(point.y for point in points),
            max_x=max(point.x for point in points),
            max_y=max(point.y for point in points),
        )

        new_heading = (
                heading_degrees + extent_degrees
        )

        return (
            end_position,
            new_heading,
            bounds,
        )

    def calculate_bounds(
        self,
        commands: Iterable[DrawingCommand],
    ) -> BoundingBox:

        position = Point2D(0.0, 0.0)
        heading_degrees = 0.0

        min_x = max_x = position.x
        min_y = max_y = position.y

        for command in commands:

            match command:

                case Forward(distance):

                    heading_radians = math.radians(
                        heading_degrees
                    )

                    position = Point2D(
                        x=position.x
                        + distance * math.cos(heading_radians),

                        y=position.y
                        + distance * math.sin(heading_radians),
                    )

                    min_x = min(min_x, position.x)
                    max_x = max(max_x, position.x)

                    min_y = min(min_y, position.y)
                    max_y = max(max_y, position.y)

                case Turn(direction, angle_degrees):

                    if direction is TurnDirection.LEFT:
                        heading_degrees += angle_degrees
                    else:
                        heading_degrees -= angle_degrees

                case Arc(radius, angle_degrees):

                    (
                        position,
                        heading_degrees,
                        arc_bounds,
                    ) = self._analyze_arc(
                        position,
                        heading_degrees,
                        radius,
                        angle_degrees,
                    )

                    min_x = min(min_x, arc_bounds.min_x)
                    max_x = max(max_x, arc_bounds.max_x)

                    min_y = min(min_y, arc_bounds.min_y)
                    max_y = max(max_y, arc_bounds.max_y)

        return BoundingBox(
            min_x=min_x,
            min_y=min_y,
            max_x=max_x,
            max_y=max_y,
        )