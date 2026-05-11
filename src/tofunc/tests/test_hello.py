import functools
import unittest
from typing import Any, Self

from tofunc import tofunc

__all__ = ["TestHello"]


class Bar:
    def join(self: Self, b: Any = "beta", c: Any = "gamma") -> str:
        return "%s %s %s" % (self, b, c)


class TestHello(unittest.TestCase):
    def test_hello(self: Self) -> None:

        class Foo:
            greet: Any

            def __str__(self: Self) -> str:
                return "Foo"

        text: str
        Foo.greet = functools.partial(Bar.join, c="hello")
        self.assertEqual(Foo().greet("Alice"), "Alice beta hello")
        Foo.greet = tofunc(Foo.greet)
        self.assertEqual(Foo().greet("Bob"), "Foo Bob hello")


if __name__ == "__main__":
    unittest.main()
