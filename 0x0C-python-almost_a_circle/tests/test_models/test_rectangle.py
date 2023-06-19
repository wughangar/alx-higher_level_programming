from io import StringIO
import unittest
import sys
sys.path.append('..')
from unittest.mock import patch
from models.rectangle import Rectangle

"""
test cases for child class rectangle inheriting from base class
"""

class TestRectangle(unittest.TestCase):
    #test for tes_constructor method
    #test for valid initialization values
    def test_constructor(self):
        r = Rectangle(5, 11, 3, 5)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 11)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 2)

    #test for area
    def test_area(self):
        r = Rectangle(5, 11)
        self.assertEqual(r.area(), 55)

    #test for display
    def test_display(self):
        r = Rectangle(5, 4)
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    #test for updates
    def test_update(self):
        r = Rectangle(5, 11, 3, 5)
        r.update(1, 7, 8, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 11)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 5)

        r.update(width=3, x=1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.x, 1)

    #test for str method
    def test_str(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1)2/3 -5 / 10"
        self.assertEqual(str(r), expected_output)

if __name__ == '__main__':
    unittest.main()



