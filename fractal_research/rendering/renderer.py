from abc import ABC, abstractmethod
from collections.abc import Iterable

from fractal_research.core.drawing_commands import DrawingCommand
from fractal_research.core.geometry import Point2D


class Renderer(ABC):
    """Defines the interface for fractal renderers."""

    @abstractmethod
    def move_to(self, point: Point2D) -> None:
        """Moves to the initial drawing position."""
        pass

    @abstractmethod
    def render(
        self,
        commands: Iterable[DrawingCommand],
    ) -> None:
        """Renders a sequence of drawing commands."""
        pass

    @abstractmethod
    def finish(self) -> None:
        """Finalizes the rendering process."""
        pass