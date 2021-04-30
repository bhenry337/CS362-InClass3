import unittest
import calc
class TestCase(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(calc.add(2,3),5)

	def test_diff(self):
		self.assertEqual(calc.diff(5,3), 2)

	def test_multiply(self):
		self.assertEqual(calc.mult(5,5), 25)

	def test_div(self):
		self.assertEqual(calc.div(6,3), 2)
