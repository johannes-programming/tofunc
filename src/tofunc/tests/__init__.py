"""Run all tests of the tofunc project."""

__all__: list[str] = ["test"]

import unittest


def test() -> unittest.TextTestResult:
    """Run all the tests."""
    loader: unittest.TestLoader
    suite: unittest.TestSuite
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tofunc.tests")
    return unittest.TextTestRunner().run(suite)
