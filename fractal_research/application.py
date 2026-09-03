from fractal_research.fractals.puzzle.puzzle_fractal import (
    PuzzleFractal,
)
from fractal_research.rendering.renderer import Renderer


class FractalApplication:
    """Coordinates fractal generation and rendering."""

    def __init__(
        self,
        fractal: PuzzleFractal,
        renderer: Renderer,
    ):
        self.fractal = fractal
        self.renderer = renderer

    def run(self) -> None:
        commands = self.fractal.generate()

        self.renderer.move_to(
            self.fractal.start_position
        )

        self.renderer.render(commands)
        self.renderer.finish()