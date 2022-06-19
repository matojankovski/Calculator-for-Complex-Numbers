
#NOT FINISHED RLC MODULE


import unittest
from ComplexLogic import Calculator
import mock


class MyTestCase(unittest.TestCase):

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
        mocked_input.side_effect = ["2.5k", "2.25m", "1.6u", "1k", "200", "1.5"]  # , "-1.5"]
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
        num = ComplexNumber(5, 6)
        print("Number:", num)
