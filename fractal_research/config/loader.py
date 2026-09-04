import json
import math
from pathlib import Path
from typing import Any

from fractal_research.config.errors import ConfigValidationError
from fractal_research.config.settings import PuzzleFractalConfig
from fractal_research.core.drawing_commands import TurnDirection
from fractal_research.fractals.puzzle.side_pattern import (
    ArcRule,
    ForwardRule,
    RecursiveSide,
    SidePatternConfig,
    SideRule,
    TurnRule,
)


class PuzzleFractalConfigLoader:
    """Loads and validates Puzzle Fractal configurations from JSON."""

    REQUIRED_FIELDS = {
        "id",
        "side_count",
        "recursion_depth",
        "base_side_length",
        "scale_factor",
        "operations",
    }

    @classmethod
    def load(
        cls,
        file_path: str | Path,
    ) -> PuzzleFractalConfig:
        """Loads a Puzzle Fractal configuration from a JSON file."""

        path = Path(file_path)

        if not path.exists():
            raise ConfigValidationError(
                f"Configuration file does not exist: {path}"
            )

        try:
            with path.open(
                mode="r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

        except json.JSONDecodeError as error:
            raise ConfigValidationError(
                f"Invalid JSON in '{path}': {error}"
            ) from error

        if not isinstance(data, dict):
            raise ConfigValidationError(
                "The root JSON value must be an object."
            )

        cls._validate_fields(data)

        side_pattern = cls._parse_side_pattern(
            data["operations"]
        )

        return PuzzleFractalConfig(
            id=cls._validate_id(data["id"]),
            side_count=cls._require_integer(
                data["side_count"],
                "side_count",
            ),
            recursion_depth=cls._require_integer(
                data["recursion_depth"],
                "recursion_depth",
            ),
            base_side_length=cls._require_number(
                data["base_side_length"],
                "base_side_length",
            ),
            scale_factor=cls._require_number(
                data["scale_factor"],
                "scale_factor",
            ),
            side_pattern=side_pattern,
        )

    @classmethod
    def _validate_fields(
        cls,
        data: dict[str, Any],
    ) -> None:
        """Ensures that all required configuration fields exist."""

        missing_fields = (
            cls.REQUIRED_FIELDS - data.keys()
        )

        if missing_fields:
            missing = ", ".join(
                sorted(missing_fields)
            )

            raise ConfigValidationError(
                f"Missing configuration field(s): {missing}"
            )

    @classmethod
    def _parse_side_pattern(
        cls,
        operations: Any,
    ) -> SidePatternConfig:
        """Converts JSON operations into side rule objects."""

        if not isinstance(operations, list):
            raise ConfigValidationError(
                "'operations' must be a JSON array."
            )

        if not operations:
            raise ConfigValidationError(
                "'operations' cannot be empty."
            )

        parsed_operations: list[SideRule] = []

        for index, operation in enumerate(operations):
            parsed_operations.append(
                cls._parse_operation(
                    operation,
                    index,
                )
            )

        return SidePatternConfig(
            operations=tuple(parsed_operations)
        )

    @classmethod
    def _parse_operation(
        cls,
        operation: Any,
        index: int,
    ) -> SideRule:
        """Parses a single compact fractal operation."""

        if not isinstance(operation, list):
            raise ConfigValidationError(
                f"Operation {index} must be an array."
            )

        if not operation:
            raise ConfigValidationError(
                f"Operation {index} cannot be empty."
            )

        operation_name = operation[0]

        if not isinstance(operation_name, str):
            raise ConfigValidationError(
                f"Operation {index} must start with a string name."
            )

        match operation_name:

            case "recursive_side":
                cls._require_argument_count(
                    operation,
                    expected=1,
                    index=index,
                )

                return RecursiveSide()

            case "forward":
                cls._require_argument_count(
                    operation,
                    expected=2,
                    index=index,
                )

                length_factor = cls._require_number(
                    operation[1],
                    f"operations[{index}].length_factor",
                )

                if length_factor <= 0:
                    raise ConfigValidationError(
                        f"Operation {index}: "
                        "forward length_factor must be greater than zero."
                    )

                return ForwardRule(
                    length_factor=length_factor
                )

            case "turn_left":
                return cls._parse_turn(
                    operation=operation,
                    index=index,
                    direction=TurnDirection.LEFT,
                )

            case "turn_right":
                return cls._parse_turn(
                    operation=operation,
                    index=index,
                    direction=TurnDirection.RIGHT,
                )

            case "arc":
                cls._require_argument_count(
                    operation,
                    expected=3,
                    index=index,
                )

                radius_factor = cls._require_number(
                    operation[1],
                    f"operations[{index}].radius_factor",
                )

                angle_degrees = cls._require_number(
                    operation[2],
                    f"operations[{index}].angle_degrees",
                )

                if radius_factor == 0:
                    raise ConfigValidationError(
                        f"Operation {index}: "
                        "arc radius_factor cannot be zero."
                    )

                return ArcRule(
                    radius_factor=radius_factor,
                    angle_degrees=angle_degrees,
                )

            case _:
                raise ConfigValidationError(
                    f"Unknown operation '{operation_name}' "
                    f"at index {index}."
                )

    @classmethod
    def _parse_turn(
        cls,
        operation: list[Any],
        index: int,
        direction: TurnDirection,
    ) -> TurnRule:

        cls._require_argument_count(
            operation,
            expected=2,
            index=index,
        )

        angle_degrees = cls._require_number(
            operation[1],
            f"operations[{index}].angle_degrees",
        )

        return TurnRule(
            direction=direction,
            angle_degrees=angle_degrees,
        )

    @staticmethod
    def _require_argument_count(
        operation: list[Any],
        expected: int,
        index: int,
    ) -> None:

        if len(operation) != expected:
            raise ConfigValidationError(
                f"Operation {index} expects "
                f"{expected - 1} argument(s), "
                f"but received {len(operation) - 1}."
            )

    @staticmethod
    def _require_integer(
        value: Any,
        field_name: str,
    ) -> int:

        if isinstance(value, bool) or not isinstance(value, int):
            raise ConfigValidationError(
                f"'{field_name}' must be an integer."
            )

        return value

    @staticmethod
    def _require_number(
        value: Any,
        field_name: str,
    ) -> float:

        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            raise ConfigValidationError(
                f"'{field_name}' must be numeric."
            )

        number = float(value)

        if not math.isfinite(number):
            raise ConfigValidationError(
                f"'{field_name}' must be finite."
            )

        return number

    @staticmethod
    def _validate_id(
        value: Any,
    ) -> str:
        """Validates a 32-character hexadecimal UUID representation."""

        if not isinstance(value, str):
            raise ConfigValidationError(
                "'id' must be a string."
            )

        if len(value) != 32:
            raise ConfigValidationError(
                "'id' must contain exactly 32 hexadecimal characters."
            )

        try:
            int(value, 16)

        except ValueError as error:
            raise ConfigValidationError(
                "'id' must contain only hexadecimal characters."
            ) from error

        return value.lower()