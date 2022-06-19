import unittest
import io
from ComplexLogic import Calculator, RLC
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


    # @mock.patch("ComplexLogic.input", create=True)
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

    def testAddComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(5, 5)
        self.assertEqual(calculator.AddComplexNumbers(), ComplexNumber(10,10))





    def testDivide(self):
        number1 = ComplexNumber(5, 5)
        self.assertEqual(number1.Divide(ComplexNumber(1,1)),  ComplexNumber(5,0))
        number2 = ComplexNumber(5, 5)
        self.assertEqual(number2.Divide(ComplexNumber(2.5, -2.5)), ComplexNumber(0, 2))
        number3 = ComplexNumber(5, 5)
        self.assertRaises(ZeroDivisionError, number3.Divide, ComplexNumber(0, 0))

    def testDivideComplexNumbers(self):
        calculator = Calculator()
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(2, 2)
        self.assertEqual(calculator.DivideComplexNumbers(), ComplexNumber(2.5, 0))
        calculator.first_complex_number = ComplexNumber(5, 5)
        calculator.second_complex_number = ComplexNumber(0, 0)
        # self.assertRaises(ZeroDivisionError, calculator.DivideComplexNumbers)


        # number4 = ComplexNumber(5,5)
        # self.assertEqual(number4.Divide(ComplexNumber(0,0)), ComplexNumber(0,0))








    # def testAddComplexNumbers(self):
    #     calculator = Calculator()
    #     first_complex_number = ComplexNumber(-5,5)
    #     secondcomplexnumber = ComplexNumber(-5, -5)
    #     self.assertEqual(calculator.AddComplexNumbers(), (0,0))




    def testSubtract(self):
        number1 = ComplexNumber(-5, -5)
        self.assertEqual(number1.Subtract(ComplexNumber(5, 5)),  ComplexNumber(-10, -10))
        number2 = ComplexNumber(-5, -5)
        self.assertEqual(number2.Subtract(ComplexNumber(-8, 5)),  ComplexNumber(3, -10))
        number3 = ComplexNumber(-5, -5)
        self.assertEqual(number3.Subtract(ComplexNumber(-2, 5)),  ComplexNumber(-3, -10))
        number4 = ComplexNumber(0, 0)
        self.assertEqual(number4.Subtract(ComplexNumber(-2, 5)), ComplexNumber(2, -5))

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










    # @mock.patch('sys.stdout', new_callable=io.StringIO)
    # @mock.patch("ComplexLogic.input", create=True)
    # def test_GetComplexNumber1(self, mocked_input, expected_output, mocked_output):
    #     calculator = Calculator()
    #     mocked_input.side_effect = [".4i"]
    #     re, im = calculator.GetComplexNumber()
    #     expected_output = "WRONG INPUT"
    #     self.assertEqual(mocked_output.getvalue(), expected_output)
    #
    #

    # @mock.patch('sys.stdout', new_callable=io.StringIO)
    # def test_testujemPrint(self, expected_output, mocked_output):
    #     c = Calculator()
    #     c.a = 5
    #     c.testujemPrint()
    #     expected_output = "Hello there"
    #     self.assertEqual(mocked_output.getvalue(), expected_output)
    #




    def test_DisplayResultNumberInString(self):
        calculator = Calculator()
        calculator.realResult = 4.5
        calculator.imgResult = 4.5
        s = calculator.DisplayResultNumberInString()
        self.assertEqual(s, "Rectangular form : 4.5+4.5i")
        calculator.realResult = -4.5
        calculator.imgResult = -4.5
        s = calculator.DisplayResultNumberInString()
        self.assertEqual(s, "Rectangular form : -4.5-4.5i")
        calculator.realResult = -4.5
        calculator.imgResult = 4.5
        s = calculator.DisplayResultNumberInString()
        self.assertEqual(s, "Rectangular form : -4.5+4.5i")
        calculator.realResult = 4.5
        calculator.imgResult = -4.5
        s = calculator.DisplayResultNumberInString()
        self.assertEqual(s, "Rectangular form : 4.5-4.5i")
        calculator.realResult = 0
        calculator.imgResult = -4.5
        s = calculator.DisplayResultNumberInString()
        self.assertEqual(s, "Rectangular form : 0-4.5i")
        calculator.realResult = -4.5
        calculator.imgResult = 0
        s = calculator.DisplayResultNumberInString()
        self.assertEqual(s, "Rectangular form : -4.5+0i")

    def test_AddComplexNumbers(self):
        calculator = Calculator()
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, 4.5, 4.5, 4.5
        self.assertEqual(calculator.AddComplexNumbers(), [9, 9])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, -4.5, 4.5, 4.5
        self.assertEqual(calculator.AddComplexNumbers(), [9, 0])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, -4.5, -4.5, -4.5
        self.assertEqual(calculator.AddComplexNumbers(), [0, -9])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = -4.5, -4.5, -4.5, -4.5
        self.assertEqual(calculator.AddComplexNumbers(), [-9, -9])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 0, -4.5, 0, -4.5
        self.assertEqual(calculator.AddComplexNumbers(), [0, -9])

    def test_SubtrackComplexNumbers(self):
        calculator = Calculator()
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, 4.5, 4.5, 4.5
        self.assertEqual(calculator.SubtrackComplexNumbers(), [0, 0])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, -4.5, 4.5, 4.5
        self.assertEqual(calculator.SubtrackComplexNumbers(), [0, -9])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, -4.5, -4.5, -4.5
        self.assertEqual(calculator.SubtrackComplexNumbers(), [9, 0])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = -4.5, -4.5, -4.5, -4.5
        self.assertEqual(calculator.SubtrackComplexNumbers(), [0, 0])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 0, -4.5, 0, -4.5
        self.assertEqual(calculator.SubtrackComplexNumbers(), [0, 0])

    def test_MultiplyComplexNumbers(self):
        calculator = Calculator()
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, 4.5, 4.5, 4.5
        self.assertEqual(calculator.MultiplyComplexNumbers(), [0, 40.5])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, -4.5, 4.5, 4.5
        self.assertEqual(calculator.MultiplyComplexNumbers(), [40.5, 0])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, -4.5, -4.5, -4.5
        self.assertEqual(calculator.MultiplyComplexNumbers(), [-40.5, 0])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = -4.5, -4.5, -4.5, -4.5
        self.assertEqual(calculator.MultiplyComplexNumbers(), [0, 40.5])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 0, -4.5, 0, -4.5
        self.assertEqual(calculator.MultiplyComplexNumbers(), [-20.25, 0])

    def test_DivideComplexNumbers(self):
        calculator = Calculator()
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, 4.2, 4.2, 4.5
        self.assertEqual(calculator.DivideComplexNumbers(), [0.998, -0.069])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, -4.2, 4.2, 4.5
        self.assertEqual(calculator.DivideComplexNumbers(), [0, -1])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 4.5, -4.2, -4.2, -4.5
        self.assertEqual(calculator.DivideComplexNumbers(), [0, 1])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = -4.5, -4.2, -4.2, -4.5
        self.assertEqual(calculator.DivideComplexNumbers(), [0.998, -0.069])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 0, -4.5, 0, -4.5
        self.assertEqual(calculator.DivideComplexNumbers(), [1, 0])
        calculator.re1, calculator.img1, calculator.re2, calculator.img2 = 0, 0, 0, 0
        self.assertEqual(calculator.DivideComplexNumbers(), "Division by Zero!")   #ako vyriesit toto










    def test_GetPolarForm(self):
        calculator = Calculator()
        calculator.realResult, calculator.imgResult = 4.2, 2.2
        self.assertEqual(calculator.GetPolarForm(), (4.74, 27.65))
        calculator.realResult, calculator.imgResult = 4.2, -2.2
        self.assertEqual(calculator.GetPolarForm(), (4.74, -27.65))
        calculator.realResult, calculator.imgResult = -4.2, 2.2
        self.assertEqual(calculator.GetPolarForm(), (4.74, -27.65))
        calculator.realResult, calculator.imgResult = 2.2, 4.2
        self.assertEqual(calculator.GetPolarForm(), (4.74, 62.35))
        calculator.realResult, calculator.imgResult = -2.2, 4.2
        self.assertEqual(calculator.GetPolarForm(), (4.74, -62.35))
        calculator.realResult, calculator.imgResult = -2.2, -4.2
        self.assertEqual(calculator.GetPolarForm(), (4.74, 62.35))
        calculator.realResult, calculator.imgResult = -4.2, -2.2
        self.assertEqual(calculator.GetPolarForm(), (4.74, 27.65))
        calculator.realResult, calculator.imgResult = -4.2, 0
        self.assertEqual(calculator.GetPolarForm(), (4.2, 0))
        calculator.realResult, calculator.imgResult = 0, 4.2
        self.assertEqual(calculator.GetPolarForm(), "Division by Zero Error")

    def test_DisplayInPolarForm(self):
        calculator = Calculator()
        self.modulus, self.phase = 5, 22
        self.assertEqual(calculator.DisplayInPolarForm(), "5∠22°")





    @mock.patch("ComplexLogic.input", create=True)
    def test_GetValue(self, mocked_input):
        mocked_input.side_effect = ["2.5k", "2.25m", "1.6u", "1k", "200", "1.5", "-1.5", "Hello"]
        rlccalculator = RLC()
        self.assertEqual(rlccalculator.GetValue(), 2500)
        self.assertEqual(rlccalculator.GetValue(), 0.00225)
        self.assertEqual(rlccalculator.GetValue(), 1.6e-6)
        self.assertEqual(rlccalculator.GetValue(), 1000)
        self.assertEqual(rlccalculator.GetValue(), 200)
        self.assertEqual(rlccalculator.GetValue(), 1.5)
        self.assertEqual(rlccalculator.GetValue(), -1.5)
        self.assertEqual(rlccalculator.GetValue(), 2500)





    def test_GetInPolarForm(self):
        rlccalculator = RLC()
        rlccalculator.realResult, rlccalculator.imgResult = 4.2, 2.2
        self.assertEqual(rlccalculator.GetInPolarForm(), "4.74Ω ∠27.65°")
        rlccalculator.realResult, rlccalculator.imgResult = 4.2, 2.2
        self.assertEqual(rlccalculator.GetInPolarForm(), "4.74Ω ∠27.65°")




    def test_WriteInString(self):
        rlccalculator = RLC()
        result = "12000"
        self.assertEqual(rlccalculator.WriteInString(result), "12.0kΩ")
        result = "12500"
        self.assertEqual(rlccalculator.WriteInString(result), "12.5kΩ")
        result = "12550"
        self.assertEqual(rlccalculator.WriteInString(result), "12.5kΩ")

    # def test_GetImpedanceOfSeriesConnection(self):
    #     rlccalculator = RLC()

    @mock.patch("ComplexLogic.input", create=True)
    def test_GetZofResistor(self, mocked_input):
        mocked_input.side_effect = ["2.5k", "2.25m", "1.6u", "1k", "200", "1.5"]#, "-1.5"]
        rlccalculator = RLC()
        self.assertEqual(rlccalculator.GetZofResistor(), (2500.0, 0))
        self.assertEqual(rlccalculator.GetZofResistor(), (0.00225, 0))
        self.assertEqual(rlccalculator.GetZofResistor(), (0.0000016, 0))
        self.assertEqual(rlccalculator.GetZofResistor(), (1000, 0))
        self.assertEqual(rlccalculator.GetZofResistor(), (200, 0))
        self.assertEqual(rlccalculator.GetZofResistor(), (1.5, 0))
        # self.assertEqual(rlccalculator.GetZofResistor(), (-1.5, 0))






    @mock.patch("ComplexLogic.input", create=True)
    def test_GetZofInductor(self, mocked_input):
        mocked_input.side_effect = ["2.5m", "1k", "1.6u", "1k"]
        rlccalculator = RLC()
        self.assertEqual(rlccalculator.GetZofInductor(), (0, 15.70796327))
        self.assertEqual(rlccalculator.GetZofInductor(), (0, 0.0100531))

    @mock.patch("ComplexLogic.input", create=True)
    def test_GetZofCapacitor(self, mocked_input):
        mocked_input.side_effect = ["6.2u", "0.05k", "100.5u", "1.5k", "9.2u", "5.5k", "5.5k", "0m"]
        rlccalculator = RLC()
        self.assertEqual(rlccalculator.GetZofCapacitor(), (0, -513.40304223))
        self.assertEqual(rlccalculator.GetZofCapacitor(), (0, -1.05575418))
        self.assertEqual(rlccalculator.GetZofCapacitor(), (0, -3.14535461))
        self.assertEqual(rlccalculator.GetZofCapacitor(), "Division by Zero. Enter correct values!")


    # def test_GetImpedanceOfSeriesConnection(self):


    def test_tmp(self):
        num = ComplexNumber(5,6)
        print("Number:", num)









    # def test_GetZofInductor(self):


    # def test_GetZofCapacitor(self):
    #     rlccalculator = RLC()
























    # @mock.patch("ComplexLogic.input", create=True)
    # def test_AddComplexNumbers(self, mocked_input):
    #     mocked_input.side_effect = ["2.2+2.2i", "2.2+2.2i", "2.2", "2.2+2.2i", "-4.2", "-4.2", "0+0i","0+0i"]
    #     calculator = Calculator()
    #     result = calculator.AddComplexNumbers()
    #     self.assertEqual(result, [4.4, 4.4])
    #     result = calculator.AddComplexNumbers()
    #     self.assertEqual(result, [4.4, 2.2])
    #     result = calculator.AddComplexNumbers()
    #     self.assertEqual(result, [-8.4, 0])
    #     result = calculator.AddComplexNumbers()
    #     self.assertEqual(result, [0, 0])

    # @mock.patch("ComplexLogic.input", create=True)
    # def test_SubtrackComplexNumbers(self, mocked_input):
    #     mocked_input.side_effect = ["2.2+2.2i", "2.2+2.2i", "2.2", "2.2+2.2i", "-4.2", "-4.2", "-2.4-2.3i", "-4.2-4.5i"]
    #     calculator = Calculator()
    #     result = calculator.SubtrackComplexNumbers()
    #     self.assertEqual(result, [0, 0])
    #     result = calculator.SubtrackComplexNumbers()
    #     self.assertEqual(result, [0, -2.2])
    #     result = calculator.SubtrackComplexNumbers()
    #     self.assertEqual(result, [0, 0])
    #     result = calculator.SubtrackComplexNumbers()
    #     self.assertEqual(result, [1.8, 2.2])

    # @mock.patch("ComplexLogic.input", create=True)
    # def test_MultiplyComplexNumbers(self, mocked_input):
    #     mocked_input.side_effect = ["2.2+2.2i", "2.2+2.2i", "2.2", "2.2+2.2i", "-4.2", "-4.2", "-5i","5i"]
    #     calculator = Calculator()
    #     result = calculator.MultiplyComplexNumbers()
    #     self.assertEqual(result, [0.0, 9.68])
    #     #2.2 * (2.2+2.2i)
    #     result = calculator.MultiplyComplexNumbers()
    #     self.assertEqual(result, [4.84, 4.84])
    #     #-4.2 * -4.2
    #     result = calculator.MultiplyComplexNumbers()
    #     self.assertEqual(result, [17.64, 0])
    #     #0+0i * 0+0i
    #     result = calculator.MultiplyComplexNumbers()
    #     self.assertEqual(result, [25, 0])

    # @mock.patch("ComplexLogic.input", create=True)
    # def test_DivideComplexNumbers(self, mocked_input):
    #     mocked_input.side_effect = ["2.2+2.2i", "2.2+2.2i", "0+5i", "0+5i", "10+2i", "-4+2i", "4+4i", "2+2i"]
    #     calculator = Calculator()
    #     result = calculator.DivideComplexNumbers()
    #     self.assertEqual(result, [1, 0])
    #     result = calculator.DivideComplexNumbers()
    #     self.assertEqual(result, [1, 0])
    #     result = calculator.DivideComplexNumbers()
    #     self.assertEqual(result, [-1.8, -1.4])
    #     result = calculator.DivideComplexNumbers()
    #     self.assertEqual(result, [2, 0])

    # def test_DisplayResultNumberInString(self):
    #     calculator = Calculator()
    #     calculator.real_result = 4.5
    #     calculator.imag_result = 4.5
    #     result = calculator.DisplayResultNumberInString()
    #     self.assertEqual(result, "4.5+4.5i")
    #     calculator.real_result = 4.5
    #     calculator.imag_result = -4.5
    #     result = calculator.DisplayResultNumberInString()
    #     self.assertEqual(result, "4.5-4.5i")
    #     calculator.real_result = -4.5
    #     calculator.imag_result = -4.5
    #     result = calculator.DisplayResultNumberInString()
    #     self.assertEqual(result, "-4.5-4.5i")
    #     calculator.real_result = -4.5
    #     calculator.imag_result = 0
    #     result = calculator.DisplayResultNumberInString()
    #     self.assertEqual(result, "-4.5+0i")
    #     calculator.real_result = 0
    #     calculator.imag_result = -4.5
    #     result = calculator.DisplayResultNumberInString()
    #     self.assertEqual(result, "0-4.5i")

if __name__ == '__main__':
    unittest.main()
