import math

from dataclasses import dataclass
from fractal_research.config.settings import CanvasConfig
from fractal_research.core.geometry import BoundingBox, Point2D


@dataclass(frozen=True, slots=True)
class AutoFitResult:
    """Contains the calculated parameters for fitting geometry."""

    start_position: Point2D
    scale_factor: float


class AutoFitLayout:
    """Scales and centers generated geometry inside a canvas."""

    def __init__(self, canvas_config: CanvasConfig):
        self.canvas_config = canvas_config

    def calculate(
        self,
        bounds: BoundingBox,
    ) -> AutoFitResult:

        available_width = (
            self.canvas_config.width
            - 2 * self.canvas_config.padding
        )

        available_height = (
            self.canvas_config.height
            - 2 * self.canvas_config.padding
        )

        scale_x = (
            available_width / bounds.width
            if bounds.width > 0
            else math.inf
        )

        scale_y = (
            available_height / bounds.height
            if bounds.height > 0
            else math.inf
        )

        scale_factor = min(
            scale_x,
            scale_y,
        )

        if math.isinf(scale_factor):
            scale_factor = 1.0

        scaled_center = Point2D(
            x=bounds.center.x * scale_factor,
            y=bounds.center.y * scale_factor,
        )

        start_position = Point2D(
            x=-scaled_center.x,
            y=-scaled_center.y,
        )

        return AutoFitResult(
            start_position=start_position,
            scale_factor=scale_factor,
        )