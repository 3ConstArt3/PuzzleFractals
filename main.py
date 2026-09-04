from pathlib import Path

from fractal_research.application import FractalApplication
from fractal_research.config.loader import PuzzleFractalConfigLoader
from fractal_research.config.settings import ApplicationConfig
from fractal_research.fractals.puzzle.puzzle_fractal import (
    PuzzleFractal,
)
from fractal_research.layout.auto_fit_layout import AutoFitLayout
from fractal_research.rendering.turtle_renderer import (
    TurtleRenderer,
)


def main() -> None:

    project_root = Path(__file__).resolve().parent

    config_path = (
        project_root
        / "configs"
        / "puzzle_default.json"
    )

    fractal_config = PuzzleFractalConfigLoader.load(
        config_path
    )

    config = ApplicationConfig(
        fractal=fractal_config
    )

    fractal = PuzzleFractal(
        config=config.fractal
    )

    renderer = TurtleRenderer(
        canvas_config=config.canvas,
        turtle_config=config.turtle,
    )

    layout = AutoFitLayout(
        canvas_config=config.canvas
    )

    renderer.configure()

    application = FractalApplication(
        fractal=fractal,
        renderer=renderer,
        layout=layout,
    )

    application.run()


if __name__ == "__main__":
    main()