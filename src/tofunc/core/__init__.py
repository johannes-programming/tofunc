"""Convert any callable into a function."""

__all__: list[str] = ["tofunc"]

import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar

Params = ParamSpec("Params")
Return = TypeVar("Return")


def tofunc(old: Callable[Params, Return], /) -> Callable[Params, Return]:
    """Convert the given callable into a function."""

    def new(*args: Params.args, **kwargs: Params.kwargs) -> Return:
        """Call the original with given args and kwargs."""
        return old(*args, **kwargs)

    try:
        return functools.wraps(old)(new)
    except Exception:
        return new
