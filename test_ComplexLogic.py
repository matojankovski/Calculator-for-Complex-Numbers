import unittest
from ComplexLogic import Calculator
import mock

from ComplexNumber import ComplexNumber


class MyTestCase(unittest.TestCase):


    def test_ParseComplexNumer(self):
        self.assertEqual(ComplexNumber.ParseComplexNumer("4.5-5.7i"), ComplexNumber(4.5, -5.7))
        self.assertEqual(ComplexNumber.ParseComplexNumer("-1i"), ComplexNumber(0, -1))
        self.assertEqual(ComplexNumber.ParseComplexNumer("-i"), ComplexNumber(0, -1))
        self.assertEqual(ComplexNumber.ParseComplexNumer("-5.5"), ComplexNumber(-5.5, 0))
        self.assertEqual(ComplexNumber.ParseComplexNumer("0-5i"), ComplexNumber(0, -5))
        self.assertRaises(AttributeError, ComplexNumber.ParseComplexNumer, "abc")
        self.assertRaises(AttributeError, ComplexNumber.ParseComplexNumer, "*")
        self.assertRaises(AttributeError, ComplexNumber.ParseComplexNumer, "+")

    @mock.patch("builtins.input", create=True)
    def test_GetComplexNumber(self, mocked_input):
        mocked_input.side_effect = ["2.5", "2.5i", "-2.5", "-2.5i", "2.5+2.5i", "-2.5-2.5i", "0+0i", "j", ".4i", "i", "2+i", "2-i", "0-5i"]
        calculator = Calculator()
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(2.5, 0))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(0, 2.5))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(-2.5, 0))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(0, -2.5))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(2.5, 2.5))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(-2.5, -2.5))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(0, 0))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(0,1))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(0, 0.4))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(0, 1))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(2, 1))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(2, -1))
        self.assertEqual(calculator.GetComplexNumber(), ComplexNumber(0, -5))

    def testAdd(self):
        number1 = ComplexNumber(5, 5)
        self.assertEqual(number1.Add(ComplexNumber(5.2, 5.3)),  ComplexNumber(10.2, 10.3))
        number2 = ComplexNumber(-5, -5)
        self.assertEqual(number2.Add(ComplexNumber(-5, -5)), ComplexNumber(-10, -10))
        number3 = ComplexNumber(0, -5)
        self.assertEqual(number3.Add(ComplexNumber(-5, -4)), ComplexNumber(-5, -9))
        number4 = ComplexNumber(2.35, -5.85)
        self.assertEqual(number4.Add(ComplexNumber(3.5, 2.85)), ComplexNumber(5.85, -3))

    def testAddComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.AddComplexNumbers(), ComplexNumber(10,10))
        calculator.first_complex_number = ComplexNumber(-2.3, 2)
        calculator.second_complex_number = ComplexNumber(-2.5, -5.3)
        self.assertEqual(calculator.AddComplexNumbers(), ComplexNumber(-4.8, -3.3))
        calculator.first_complex_number = ComplexNumber(-2.3, 0)
        calculator.second_complex_number = ComplexNumber(-2.5, 0)
        self.assertEqual(calculator.AddComplexNumbers(), ComplexNumber(-4.8, 0))

    def testDivide(self):
        number1 = ComplexNumber(5, 5)
        self.assertEqual(number1.Divide(ComplexNumber(1,1)),  ComplexNumber(5,0))
        number2 = ComplexNumber(5, 5)
        self.assertEqual(number2.Divide(ComplexNumber(2.5, -2.5)), ComplexNumber(0, 2))
        number3 = ComplexNumber(5, 5)
        self.assertRaises(ZeroDivisionError, number3.Divide, ComplexNumber(0, 0))
        number4 = ComplexNumber(2.5, -7.5)
        self.assertEqual(number4.Divide(ComplexNumber(-4.5, 3.25)), ComplexNumber(-1.16, 0.83))

    def testDivideComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(2, 2)
        self.assertEqual(calculator.DivideComplexNumbers(), ComplexNumber(2.5, 0))
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(2.5, -2.5)
        self.assertEqual(calculator.DivideComplexNumbers(), ComplexNumber(0,2))


    def testSubtract(self):
        number1 = ComplexNumber(-5, -5)
        self.assertEqual(number1.Subtract(ComplexNumber(5, 5)),  ComplexNumber(-10, -10))
        number2 = ComplexNumber(-5, -5)
        self.assertEqual(number2.Subtract(ComplexNumber(-8, 5)),  ComplexNumber(3, -10))
        number3 = ComplexNumber(-5, -5)
        self.assertEqual(number3.Subtract(ComplexNumber(-2, 5)),  ComplexNumber(-3, -10))
        number4 = ComplexNumber(0, 0)
        self.assertEqual(number4.Subtract(ComplexNumber(-2, 5)), ComplexNumber(2, -5))
        number5 = ComplexNumber(-5.2, -5.4)
        self.assertEqual(number5.Subtract(ComplexNumber(5.1, 5.6)), ComplexNumber(-10.3, -11.0))

    def testSubtrackComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(-5, -5)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.SubtrackComplexNumbers(), ComplexNumber(-10, -10))
        calculator.first_complex_number = ComplexNumber(-2.5, -8.5)
        calculator.second_complex_number = ComplexNumber(-4.2, 5.2)
        self.assertEqual(calculator.SubtrackComplexNumbers(), ComplexNumber(1.7, -13.7))
        calculator.first_complex_number = ComplexNumber(-2.5, -8.5)
        calculator.second_complex_number = ComplexNumber(0,0)
        self.assertEqual(calculator.SubtrackComplexNumbers(), ComplexNumber(-2.5, -8.5))

    def testMultiply(self):
        number1 = ComplexNumber(1, 1)
        self.assertEqual(number1.Multiply(ComplexNumber(5, 5)), ComplexNumber(0, 10))
        number2 = ComplexNumber(0, 0)
        self.assertEqual(number2.Multiply(ComplexNumber(5, 5)), ComplexNumber(0, 0))
        number3 = ComplexNumber(-1, -1)
        self.assertEqual(number3.Multiply(ComplexNumber(5, 5)), ComplexNumber(0, -10))
        number4 = ComplexNumber(0, -5)
        self.assertEqual(number4.Multiply(ComplexNumber(5, 5)), ComplexNumber(25, -25))
        number5 = ComplexNumber(-5, -5)
        self.assertEqual(number5.Multiply(ComplexNumber(5, 5)), ComplexNumber(0, -50))
        number5 = ComplexNumber(-5.2, -5.4)
        self.assertEqual(number5.Multiply(ComplexNumber(5.1, 5.6)), ComplexNumber(3.72, -56.66))

    def testMultiplyComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(1, 1)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.MultiplyComplexNumbers(), ComplexNumber(0,10))
        calculator.first_complex_number = ComplexNumber(0, 0)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.MultiplyComplexNumbers(), ComplexNumber(0, 0))
        calculator.first_complex_number = ComplexNumber(5.1, 5.6)
        calculator.second_complex_number = ComplexNumber(-5.2, -5.4)
        self.assertEqual(calculator.MultiplyComplexNumbers(), ComplexNumber(3.72, -56.66))

    def testDisplayInPolarForm(self):
        number1 = ComplexNumber(4.2, 2.2)
        self.assertEqual(number1.DisplayInPolarForm(), "Polar form: 4.74∠27.65°")
        number1 = ComplexNumber(4.2, -2.2)
        self.assertEqual(number1.DisplayInPolarForm(), "Polar form: 4.74∠-27.65°")
        number1 = ComplexNumber(-4.2, 2.2)
        self.assertEqual(number1.DisplayInPolarForm(), "Polar form: 4.74∠-27.65°")
        number1 = ComplexNumber(2.2, 4.2)
        self.assertEqual(number1.DisplayInPolarForm(), "Polar form: 4.74∠62.35°")
        number1 = ComplexNumber(-2.2, 4.2)
        self.assertEqual(number1.DisplayInPolarForm(), "Polar form: 4.74∠-62.35°")
        number1 = ComplexNumber(-2.2, -4.2)
        self.assertEqual(number1.DisplayInPolarForm(), "Polar form: 4.74∠62.35°")
        number1 = ComplexNumber(-4.2, -2.2)
        self.assertEqual(number1.DisplayInPolarForm(), "Polar form: 4.74∠27.65°")
        number1 = ComplexNumber(0, 5)
        self.assertEqual(number1.DisplayInPolarForm(), "This number doesn't have a polar form.")




if __name__ == '__main__':
    unittest.main()
