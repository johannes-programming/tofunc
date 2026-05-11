import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar

__all__ = ["tofunc"]

Params = ParamSpec("Params")
Return = TypeVar("Return")


def tofunc(old: Callable[Params, Return], /) -> Callable[Params, Return]:
    def new(*args: Params.args, **kwargs: Params.kwargs) -> Return:
        return old(*args, **kwargs)

    try:
        return functools.wraps(old)(new)
    except Exception:
        return new
