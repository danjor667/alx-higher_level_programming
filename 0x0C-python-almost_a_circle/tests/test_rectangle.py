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

    def test_methods(self):
        """
        doc
        """
        r2 = Rectangle(2,3, id=24)
        self.assertEqual(r2.area(), 6)
        self.assertEqual(r2.__str__(), "[Rectangle] (24) 0/0 - 2/3")

    def test_methods_update(self):
        """
        doc
        """
        r = Rectangle(10,12, id=12)
        r.update(1)
        self.assertNotEqual(r.id, 12)
        r.update(1,2)
        self.assertNotEqual(r.width, 10)
        r.update(1,2,3)
        self.assertNotEqual(r.height, 12)
        r.update(1,2,3,4)
        self.assertNotEqual(r.x, 0)
        r.update(1,2,3,4,5)
        self.assertNotEqual(r.y, 0)
        #passing now a dict to update
        self.assertNotEqual(r.id, r.update(**{"id": 89}))
        self.assertNotEqual(r.width, r.update(**{"id": 89, "width": 3}))
        self.assertNotEqual(r.height, r.update(**{"id": 89, "width": 4, "height": 21}))
        self.assertNotEqual(r.x, r.update(**{"id": 89, "width": 4, "height": 21, "x": 3}))
        self.assertNotEqual(r.y, r.update(**{"id": 89, "width": 4, "height": 21, "x": 3, "y": 6}))

    def test_to_dict(self):
        """
        doc
        """
        r = Rectangle(1, 2, id=12)
        self.assertEqual(r.to_dictionary(), {"id": 12, "x": 0, "y": 0, "width": 1, "height": 2})
