import functools
import types
import unittest
from typing import *

from tofunc import tofunc

__all__ = ["TestHello"]


class Bar:
    def join(self: Self, b: Any = "beta", c: Any = "gamma") -> str:
        return "%s %s %s" % (self, b, c)


class TestHello(unittest.TestCase):
    def test_hello(self: Self) -> None:

        class Foo:
            greet: Any

        hello: functools.partial
        hello_: types.FunctionType
        hello = functools.partial(Bar.join, c="hello")
        Foo.greet = hello
        self.assertEqual(Foo().greet("Alice"), "Alice beta hello")
        hello_ = tofunc(hello)
        Foo.greet = hello_
        text: str = Foo().greet("Bob")
        self.assertTrue(text.endswith("Bob hello"))
        self.assertTrue("Foo" in text)


if __name__ == "__main__":
    unittest.main()
