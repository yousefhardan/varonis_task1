import unittest

from dataclasses import dataclass

from magic_list import MagicList

@dataclass
class Person(object):
    age: int = 1

class magic_list_tests(unittest.TestCase):

    def test_value_0(self):
        a = MagicList()
        a[0] = 5
        assert a[0] == 5

    def test_multiple_values(self):
        a = MagicList()
        for i in range(10):
            assert a == list(range(i))
            a[i] = i

    def test_negative_index(self):
        a = MagicList()
        a[-1] = 5

    def test_multi_values_for_negative_index(self):
        a = MagicList()
        for i in range(10):
            assert a == list(range(i))
            a[-1] = i

class tests_including_initialized_types(unittest.TestCase):
    def test_magic_list_includes_initialized_types(self):
        a = MagicList(cls_type=Person)
        a[0].age = 5
        assert a[0] == Person(age=5)

    def test_magic_list_includes_assigned_types_extend_boundary_check(self):
        a = MagicList(cls_type=Person)
        with self.assertRaises(IndexError):
            a[1].age = 5


if __name__ == '__main__':
    unittest.main()