"""In-process cache for financial tool results."""

_STORE: dict = {}


def get(key):
    """Return a cached value, or None if this key has not been stored."""
    return _STORE.get(key)


def store(key, value):
    """Save a value and return it."""
    _STORE[key] = value
    return value
