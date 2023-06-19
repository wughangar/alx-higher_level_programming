import unittest
import sys
sys.path.append('..')
from unittest.mock import patch
from models.square import Square
from io import StringIO

"""
test cases for child class sqaure that inherits from rectangle
"""

class TestSquare(unittest.TestCase):
    #test fcase for constructor
    def test_constructor(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    #test for area
    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    #test for update
    def test_update(self):
        square = Square(5)
        square.update(1, 7, 4, 5)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

        square.update(size=3, x=1)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 1)

    #test for str method
    def test_str(self):
        square = Square(5)
        square.update(1, 7, 4, 5)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

        square.update(size=3, x=1)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 1)

    #test for dictionary
    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(square.to_dictionary(), expected_dict)

    #test for display
    def test_display(self):
        square = Square(5)
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            square.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
