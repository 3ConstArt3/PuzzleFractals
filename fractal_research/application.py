from fractal_research.analysis.path_analyzer import PathAnalyzer
from fractal_research.core.drawing_transforms import scale_commands
from fractal_research.fractals.puzzle.puzzle_fractal import PuzzleFractal
from fractal_research.layout.auto_fit_layout import AutoFitLayout
from fractal_research.rendering.renderer import Renderer


class FractalApplication:
    """Coordinates fractal generation, layout and rendering."""

    def __init__(
        self,
        fractal: PuzzleFractal,
        renderer: Renderer,
        layout: AutoFitLayout,
    ):
        self.fractal = fractal
        self.renderer = renderer
        self.layout = layout

        self.path_analyzer = PathAnalyzer()

    def run(self) -> None:

        bounds = self.path_analyzer.calculate_bounds(
            self.fractal.generate()
        )

        fit = self.layout.calculate(
            bounds
        )

        commands = scale_commands(
            commands=self.fractal.generate(),
            scale_factor=fit.scale_factor,
        )

        self.renderer.move_to(
            fit.start_position
        )

        self.renderer.render(
            commands
        )

        self.renderer.finish()