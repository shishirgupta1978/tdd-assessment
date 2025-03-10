import unittest
from main import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        calculator = StringCalculator()
        result = calculator.add("")
        self.assertEqual(result, 0)

    def test_single_number_string(self):
        calculator = StringCalculator()
        result = calculator.add("1")
        self.assertEqual(result, 1)

    def test_multiple_number_string(self):
        calculator = StringCalculator()
        result = calculator.add("1,5")
        self.assertEqual(result, 6)

    def test_newline_delimiter_string(self):
        calculator = StringCalculator()
        result = calculator.add("1\n2,3")
        self.assertEqual(result, 6)

    def test_custom_delimiter_string(self):
        calculator = StringCalculator()
        result = calculator.add("//;\n1;2")
        self.assertEqual(result, 3)





if __name__ == "__main__":
    unittest.main()

