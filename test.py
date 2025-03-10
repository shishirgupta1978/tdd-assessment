import unittest
from main import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        calculator = StringCalculator()
        result = calculator.add("")
        self.assertEqual(result, 0)



if __name__ == "__main__":
    unittest.main()

