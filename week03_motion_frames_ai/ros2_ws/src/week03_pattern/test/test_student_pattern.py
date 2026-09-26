import os
import unittest
from week03_pattern.pattern import build_pattern

class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        # Add assertions for your assigned pattern.
        self.assertEqual(8, len(segments))

    def test_my_pattern_order(self):
        # Check another property with a known expected result.
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        self.assertTrue(segments[0].linear_x > 0)
        self.assertTrue(segments[0].angular_z == 0)
        self.assertTrue(segments[1].angular_z > 0)
   