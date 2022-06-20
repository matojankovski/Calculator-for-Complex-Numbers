import unittest
from ComplexLogic import Calculator
import mock

from ComplexNumber import ComplexNumber


class MyTestCase(unittest.TestCase):


    def test_ParseComplexNumer(self):
        self.assertEqual(ComplexNumber.parse_complex_numer("4.5-5.7i"), ComplexNumber(4.5, -5.7))
        self.assertEqual(ComplexNumber.parse_complex_numer("-1i"), ComplexNumber(0, -1))
        self.assertEqual(ComplexNumber.parse_complex_numer("-i"), ComplexNumber(0, -1))
        self.assertEqual(ComplexNumber.parse_complex_numer("-5.5"), ComplexNumber(-5.5, 0))
        self.assertEqual(ComplexNumber.parse_complex_numer("0-5i"), ComplexNumber(0, -5))
        self.assertRaises(AttributeError, ComplexNumber.parse_complex_numer, "abc")
        self.assertRaises(AttributeError, ComplexNumber.parse_complex_numer, "*")
        self.assertRaises(AttributeError, ComplexNumber.parse_complex_numer, "+")

    @mock.patch("builtins.input", create=True)
    def test_GetComplexNumber(self, mocked_input):
        mocked_input.side_effect = ["2.5", "2.5i", "-2.5", "-2.5i", "2.5+2.5i", "-2.5-2.5i", "0+0i", "j", ".4i", "i", "2+i", "2-i", "0-5i"]
        calculator = Calculator()
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(2.5, 0))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(0, 2.5))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(-2.5, 0))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(0, -2.5))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(2.5, 2.5))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(-2.5, -2.5))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(0, 0))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(0, 1))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(0, 0.4))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(0, 1))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(2, 1))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(2, -1))
        self.assertEqual(calculator.get_complex_number(), ComplexNumber(0, -5))

    def testAdd(self):
        number1 = ComplexNumber(5, 5)
        self.assertEqual(number1.add(ComplexNumber(5.2, 5.3)), ComplexNumber(10.2, 10.3))
        number2 = ComplexNumber(-5, -5)
        self.assertEqual(number2.add(ComplexNumber(-5, -5)), ComplexNumber(-10, -10))
        number3 = ComplexNumber(0, -5)
        self.assertEqual(number3.add(ComplexNumber(-5, -4)), ComplexNumber(-5, -9))
        number4 = ComplexNumber(2.35, -5.85)
        self.assertEqual(number4.add(ComplexNumber(3.5, 2.85)), ComplexNumber(5.85, -3))

    def testAddComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.add_complex_numbers(), ComplexNumber(10, 10))
        calculator.first_complex_number = ComplexNumber(-2.3, 2)
        calculator.second_complex_number = ComplexNumber(-2.5, -5.3)
        self.assertEqual(calculator.add_complex_numbers(), ComplexNumber(-4.8, -3.3))
        calculator.first_complex_number = ComplexNumber(-2.3, 0)
        calculator.second_complex_number = ComplexNumber(-2.5, 0)
        self.assertEqual(calculator.add_complex_numbers(), ComplexNumber(-4.8, 0))

    def testDivide(self):
        number1 = ComplexNumber(5, 5)
        self.assertEqual(number1.divide(ComplexNumber(1, 1)), ComplexNumber(5, 0))
        number2 = ComplexNumber(5, 5)
        self.assertEqual(number2.divide(ComplexNumber(2.5, -2.5)), ComplexNumber(0, 2))
        number3 = ComplexNumber(5, 5)
        self.assertRaises(ZeroDivisionError, number3.divide, ComplexNumber(0, 0))
        number4 = ComplexNumber(2.5, -7.5)
        self.assertEqual(number4.divide(ComplexNumber(-4.5, 3.25)), ComplexNumber(-1.16, 0.83))

    def testDivideComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(2, 2)
        self.assertEqual(calculator.divide_complex_numbers(), ComplexNumber(2.5, 0))
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(2.5, -2.5)
        self.assertEqual(calculator.divide_complex_numbers(), ComplexNumber(0, 2))


    def testSubtract(self):
        number1 = ComplexNumber(-5, -5)
        self.assertEqual(number1.subtract(ComplexNumber(5, 5)), ComplexNumber(-10, -10))
        number2 = ComplexNumber(-5, -5)
        self.assertEqual(number2.subtract(ComplexNumber(-8, 5)), ComplexNumber(3, -10))
        number3 = ComplexNumber(-5, -5)
        self.assertEqual(number3.subtract(ComplexNumber(-2, 5)), ComplexNumber(-3, -10))
        number4 = ComplexNumber(0, 0)
        self.assertEqual(number4.subtract(ComplexNumber(-2, 5)), ComplexNumber(2, -5))
        number5 = ComplexNumber(-5.2, -5.4)
        self.assertEqual(number5.subtract(ComplexNumber(5.1, 5.6)), ComplexNumber(-10.3, -11.0))

    def testSubtrackComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(-5, -5)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.subtrack_complex_numbers(), ComplexNumber(-10, -10))
        calculator.first_complex_number = ComplexNumber(-2.5, -8.5)
        calculator.second_complex_number = ComplexNumber(-4.2, 5.2)
        self.assertEqual(calculator.subtrack_complex_numbers(), ComplexNumber(1.7, -13.7))
        calculator.first_complex_number = ComplexNumber(-2.5, -8.5)
        calculator.second_complex_number = ComplexNumber(0,0)
        self.assertEqual(calculator.subtrack_complex_numbers(), ComplexNumber(-2.5, -8.5))

    def testMultiply(self):
        number1 = ComplexNumber(1, 1)
        self.assertEqual(number1.multiply(ComplexNumber(5, 5)), ComplexNumber(0, 10))
        number2 = ComplexNumber(0, 0)
        self.assertEqual(number2.multiply(ComplexNumber(5, 5)), ComplexNumber(0, 0))
        number3 = ComplexNumber(-1, -1)
        self.assertEqual(number3.multiply(ComplexNumber(5, 5)), ComplexNumber(0, -10))
        number4 = ComplexNumber(0, -5)
        self.assertEqual(number4.multiply(ComplexNumber(5, 5)), ComplexNumber(25, -25))
        number5 = ComplexNumber(-5, -5)
        self.assertEqual(number5.multiply(ComplexNumber(5, 5)), ComplexNumber(0, -50))
        number5 = ComplexNumber(-5.2, -5.4)
        self.assertEqual(number5.multiply(ComplexNumber(5.1, 5.6)), ComplexNumber(3.72, -56.66))

    def testMultiplyComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(1, 1)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.multiply_complex_numbers(), ComplexNumber(0, 10))
        calculator.first_complex_number = ComplexNumber(0, 0)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.multiply_complex_numbers(), ComplexNumber(0, 0))
        calculator.first_complex_number = ComplexNumber(5.1, 5.6)
        calculator.second_complex_number = ComplexNumber(-5.2, -5.4)
        self.assertEqual(calculator.multiply_complex_numbers(), ComplexNumber(3.72, -56.66))

    def testDisplayInPolarForm(self):
        number1 = ComplexNumber(4.2, 2.2)
        self.assertEqual(number1.display_in_polar_form(), "Polar form: 4.7413∠27.65°")
        number1 = ComplexNumber(4.2, -2.2)
        self.assertEqual(number1.display_in_polar_form(), "Polar form: 4.7413∠-27.65°")
        number1 = ComplexNumber(-4.2, 2.2)
        self.assertEqual(number1.display_in_polar_form(), "Polar form: 4.7413∠-27.65°")
        number1 = ComplexNumber(2.2, 4.2)
        self.assertEqual(number1.display_in_polar_form(), "Polar form: 4.7413∠62.35°")
        number1 = ComplexNumber(-2.2, 4.2)
        self.assertEqual(number1.display_in_polar_form(), "Polar form: 4.7413∠-62.35°")
        number1 = ComplexNumber(-2.2, -4.2)
        self.assertEqual(number1.display_in_polar_form(), "Polar form: 4.7413∠62.35°")
        number1 = ComplexNumber(-4.2, -2.2)
        self.assertEqual(number1.display_in_polar_form(), "Polar form: 4.7413∠27.65°")
        #TODO CHECK POLAR FORM
        # number1 = ComplexNumber(0, 5)
        # self.assertEqual(number1.display_in_polar_form(), "This number doesn't have a polar form.")

    def testParseValue(self):
        self.assertEqual(ComplexNumber.parse_value("4m"), 0.004)
        self.assertEqual(ComplexNumber.parse_value("4"), 4)
        self.assertEqual(ComplexNumber.parse_value("4.5m"), 0.0045)
        self.assertEqual(ComplexNumber.parse_value("0.5"), 0.5)
        self.assertEqual(ComplexNumber.parse_value("20m"), 0.02)
        self.assertRaises(AttributeError, ComplexNumber.parse_value, "x")
        self.assertRaises(AttributeError, ComplexNumber.parse_value, "AHOJ")
        self.assertRaises(AttributeError, ComplexNumber.parse_value, "m")
        self.assertRaises(AttributeError, ComplexNumber.parse_value, ".")

    def testGetImpedance(self):
        self.assertEqual(ComplexNumber.get_impedance(200, 0), ComplexNumber(200, 0))
        self.assertEqual(ComplexNumber.get_impedance(2.5, 0), ComplexNumber(2.5, 0))
        self.assertEqual(ComplexNumber.get_impedance(0.01, 1000), ComplexNumber(0, 62.831853))
        self.assertEqual(ComplexNumber.get_impedance(2.5, 0), ComplexNumber(2.5, 0))
        self.assertEqual(ComplexNumber.get_impedance(0.01, 1000), ComplexNumber(0, 62.831853))

    # def testtestGetImpedance




if __name__ == '__main__':
    unittest.main()
