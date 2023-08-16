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

