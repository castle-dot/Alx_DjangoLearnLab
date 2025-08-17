import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -3), -4)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, -2), 1)
        self.assertEqual(self.calc.subtract(-1,1), -2)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4,2), 8)
        self.assertEqual(self.calc.multiply(-1, -3), 3)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertEqual(self.calc.multiply(-1, 0), 0)
    def test_division(self):
        self.assertEqual(self.calc.divide(4,2), 2)
        self.assertEqual(self.calc.divide(2,4), 0.5)
        self.assertEqual(self.calc.divide(5,1), 5)
        self.assertEqual(self.calc.divide(0,2), 0)
        self.assertEqual(self.calc.divide(5,0), "Error: Cannot divide by zero")






        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.



