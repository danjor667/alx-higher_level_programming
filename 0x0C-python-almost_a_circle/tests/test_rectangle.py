#!/usr/bin/python3
"""
testing rectangle
"""

import unittest
import json
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    doc
    """
    def test_rectangle(self):
        """
        doc
        """
        r1 = Rectangle(1,2)
        r2 = Rectangle(1,2,3)
        r3 = Rectangle(1,2,3,4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)

    def test_rectangle_args(self):
        """
        doc
        """
        self.assertRaises(TypeError, Rectangle, "1" ,2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -6,)
        self.assertRaises(ValueError, Rectangle, 1,2,-3,4)
        self.assertRaises(ValueError, Rectangle, 1,-2,3,4)
        self.assertRaises(ValueError,Rectangle, -1,2,3,4)
        self.assertEqual(Rectangle(1,2,3,4,5).id, 5)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle,1, 0)

    def Test_methods(self):
        """
        doc
        """
        r = Rectangle(2,2, id=24)
        self.assertEqual(r.area(), 4)
        self.assertEqual(print(r), "[Rectangle] 24 0/0 - 2/2")
