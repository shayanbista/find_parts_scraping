from typing import Callable, Optional

def safe_call(callable_fn: Callable[[], Optional[str]], default: str = "") -> str:
    try:
        return callable_fn() or default
    except Exception:
        return default