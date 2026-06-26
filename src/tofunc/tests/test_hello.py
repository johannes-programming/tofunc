"""Test the tofunc conversion on various callables including partials."""

__all__: list[str] = ["TestHello"]

import functools
import unittest
from typing import Any, Self

from tofunc import tofunc


class Bar:
    """Provide sample methods for testing callable conversion."""

    def join(self: Self, b: Any = "beta", c: Any = "gamma") -> str:
        """Join self, b and c with spaces."""
        return "%s %s %s" % (self, b, c)


class TestHello(unittest.TestCase):
    """Test tofunc on partials assigned to class attributes."""

    def test_hello(self: Self) -> None:
        """Test that wrapped partials bind self correctly."""

        class Foo:
            """Helper class for attribute binding test."""

            greet: Any

            def __str__(self: Self) -> str:
                """Return fixed repr for test."""
                return "Foo"

        Foo.greet = functools.partial(Bar.join, c="hello")
        self.assertEqual(Foo().greet("Alice"), "Alice beta hello")
        Foo.greet = tofunc(Foo.greet)
        self.assertEqual(Foo().greet("Bob"), "Foo Bob hello")


if __name__ == "__main__":
    unittest.main()
