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

    def test_negative_numbers(self):
        calculator = StringCalculator()
        with self.assertRaises(Exception) as context:
            calculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2")
    
    def test_ignore_greater_thousand_numbers(self):
        calculator = StringCalculator()
        result = calculator.add("2,1001")
        self.assertEqual(result, 2)





if __name__ == "__main__":
    unittest.main()

