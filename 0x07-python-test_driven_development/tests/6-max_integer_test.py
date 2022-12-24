#!/usr/bin/python3
"""Unittests for max_integer[]."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defining the function of the test against max_integer[]."""

    def test_ordered_list(self):
        """Test ordered list"""
        ordered = [1,2,3,4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        unordered = [1,2,4,3]
        self.assertEqual(max_integer(unordered), 4)

    def test_desc_list(self):
        """Test decsending list"""
        desc = [4,3,2,1]
        self.assertEqual(max_integer(desc), 4)

    def test_empty_list(self):
        """Test empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats(self):
        """Test floats within a list"""
        floats = [10.2, 5.5, 6.8, 20,1]
        self.assertEqual(max_integer(floats), 20.1)

    def test_ints_and_floats(self):
        """Test to find the max within int snf float datatypes"""
        ints _and_floats = [2, 13.4, 33, 15.5]
        self.assertEquals(max_integer(ints_and_floats), 33)

    def test_one_element(self):
        """Test if only there is one item"""
        one_element = [10]
        self.assertEqual(max_integer(one_element), 10)

    def test_negative_int(self):
        """Test the max integer that is negative"""
        negative_int = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative_int), -1)

if __name__ == '__main__':
    unittest.main()
