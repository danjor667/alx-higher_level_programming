#!/usr/bin/python3
"""
Tests for base class
"""
import unittest
from models.base import Base


class BaseClassTest(unittest.TestCase):
    """
    doc
    """

    def test_no_arg_base(self):
        """
        test id
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_increment(self):
        """
        is id increased
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_id_args(self):
        """
        is id set to value
        """
        b1 = Base(10)
        self.assertEqual(b1.id, Base(10).id)

    def test_id_None(self):
        """
        id id set automatically
        """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)


if __name__ == "__main__":
    unittest.main()