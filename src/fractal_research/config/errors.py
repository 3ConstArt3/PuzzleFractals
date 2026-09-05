class ConfigError(Exception):
    """Base exception for configuration-related errors."""


class ConfigValidationError(ConfigError):
    """Raised when a configuration file contains invalid data."""