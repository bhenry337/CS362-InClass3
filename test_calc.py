import unittest
import calc
class TestCase(unittest.TestCase):
	def test_sum(self):
		result = calc.add(2,3)
		self.assertEqual(result,5)

	def test_diff(self):
		result = calc.diff(5,3)
		self.assertEqual(result, 2)

	def test_multiply(self):
		result = calc.mult(5,5)
		self.assertEqual(result, 25)
