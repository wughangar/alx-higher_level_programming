from unittest.mock import patch
from models import base
import unittest
import sys
sys.path.append('..')


class Testing(unittest.TestCase):
    def test_init_no_id(self):
        obj1 = base.Base()
        obj2 = base.Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_init_no_id(self):
        obj = base.Base(15)
        self.assertEqual(obj.id, 15)

    def test_json_string(self):
        obj1 = base.Base(1)
        obj2 = base.Base(2)
        d_list = [obj1.__dict__, obj2.__dict__]

        json_string = base.Base.to_json_string(d_list)
        expected_json = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(json_string, expected_json)

    def test_empty_list(self):
        dict_list = []
        j_string = base.Base.to_json_string(dict_list)
        expected_json = '[]'
        self.assertEqual(j_string, expected_json)


if __name__ == '__main__':
    unittest.main()
