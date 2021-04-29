import unittest
import calc

def test_sum(self):
	result = calc.sum(2,3)
	self.assertEqual(result,5)

def test_diff(self):
	result = calc.difference(5,3)
	self.assertEqual(result, 2)

def test_multiply(self):
	result = calc.multiply(5,5)
	self.assertEqual(result, 25)