import uuid


def generate_hex_id() -> str:
    """Returns a unique 32-character hexadecimal identifier."""

    return uuid.uuid4().hex