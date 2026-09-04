from fractal_research.application import FractalApplication
from fractal_research.config.settings import ApplicationConfig
from fractal_research.fractals.puzzle.puzzle_fractal import PuzzleFractal
from fractal_research.layout.auto_fit_layout import AutoFitLayout
from fractal_research.rendering.turtle_renderer import TurtleRenderer


def main() -> None:

    config = ApplicationConfig()

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