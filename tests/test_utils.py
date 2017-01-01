# coding=utf-8
#!/usr/bin/env python3

"""Unit testing of utils module
"""

from utils import *

class TestUtils:
	def test_get_list(self):
		"""get_list should deserialise a json to list
		"""
		input = get_list('./tests/sample.json')
		assert isinstance(input, list)

	def test_reorder_sequence(self):
		"""reorder_sequence should return the sorting function
		"""
		input = get_list('./tests/sample.json')
		output = reorder_sequence(input, recursive_sort, iterations = 1)
		assert output == [1, 3, 2]