import math
import re

COMPLEXNUMBERPATTERN = "^(?=[iIjJ.\d+-])([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[+-]?\d+)?(?![iIjJ.\d]))?([+-]?(?:(?:\d+(?:\.\d*)?|\.\d+)(?:[+-]?\d+)?)?[iIjJ])?$"
VALUEOFELEMENT = "(\d+\.?\d*)([pmukgMG]*)"
scales = {
            "p": 0.000000000001,
            "n": 0.000000001,
            "u": 0.000001,
            "m": 0.001,
            "":  1,
            "k": 1000,
            "M": 1000000,
            "G": 1000000000
    }

class ComplexNumber:
    def __init__(self, real_part, imag_part):
        self.real_part = real_part
        self.imag_part = imag_part

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real_part == other.real_part and self.imag_part == other.imag_part
        return False

    def __repr__(self):
        return self.display_result_number_in_string()

    #method will parse number - complex number into real and imag number. Method will return class Complex number
    @staticmethod
    def parse_complex_numer(complex_number_input):
        complex_number = re.findall(COMPLEXNUMBERPATTERN, complex_number_input)
        if not complex_number:
            raise AttributeError("COULD NOT PARSE COMPLEX NUMBER")
        real_number = float(complex_number[0][0]) if complex_number[0][0] else 0
        if complex_number[0][1]:
            new_complex_number_imag = (complex_number[0][1]).translate({ord(i): None for i in 'ijIJ'})
            if new_complex_number_imag == "-" or new_complex_number_imag == "+":
                new_complex_number_imag += "1"
            imag_number = float(new_complex_number_imag) if new_complex_number_imag else 1  # into imag_number add new_complex_number_imag if it contains :something: else add 1
        else:
            imag_number = 0
        return ComplexNumber(real_number, imag_number)

    #method will parse number with unit. 4m = 0.004, etc. Invalid input will not parse
    @staticmethod
    def parse_value(element_value_input):
        element_value = re.findall(VALUEOFELEMENT, element_value_input)
        if not element_value:
            raise AttributeError("COULD NOT PARSE NUMBER")
        elif not element_value[0][0]:
            raise AttributeError("COULD NOT PARSE NUMBER")
        number = float(element_value[0][0])
        if len(element_value[0]) == 1:
            final_number = round(number, 2)
        else:
            final_number = round(number * scales[element_value[0][1]], 9)
        return final_number

    @staticmethod
    def get_sign_for_operation(sign_input):
        if sign_input == "+":
            sign = "ADD"
        elif sign_input == "-":
            sign = "SUBTRACT"
        elif sign_input == "*":
            sign = "MULTIPLY"
        elif sign_input == "/":
            sign = "DIVIDE"
        else:
            raise AttributeError("INCORRECT OPERATION SIGN")
        return sign



    @staticmethod
    def get_impedance(value, frequency):
        if frequency == 0:
            return ComplexNumber(value, 0)
        return ComplexNumber(0, round(2 * math.pi * frequency * value, 6))

    @staticmethod
    def get_admitance(value, frequency):
        if frequency == 0:
            return ComplexNumber(1/value, 0)
        return ComplexNumber(0, round(1 / (2 * math.pi * frequency * value), 6))


    def add(self, second_complex_number):
        real_result = self.real_part + second_complex_number.real_part
        imag_result = self.imag_part + second_complex_number.imag_part

        return ComplexNumber(round(real_result,6), round(imag_result,6))

    def subtract(self, second_complex_number):
        real_result = self.real_part - second_complex_number.real_part
        imag_result = self.imag_part - second_complex_number.imag_part

        return ComplexNumber(round(real_result,6), round(imag_result,6))

    def multiply(self, second_complex_number):
        real_result = (self.real_part * second_complex_number.real_part ) - (self.imag_part * second_complex_number.imag_part)
        imag_result = (self.real_part * second_complex_number.imag_part) + (self.imag_part * second_complex_number.real_part)

        return ComplexNumber(round(real_result,6), round(imag_result,6))

    def divide(self, second_complex_number):
        try:
            real_result = (self.real_part * second_complex_number.real_part + self.imag_part * second_complex_number.imag_part) / (second_complex_number.real_part ** 2 + second_complex_number.imag_part ** 2)
            imag_result = (self.imag_part * second_complex_number.real_part - self.real_part * second_complex_number.imag_part) / (second_complex_number.real_part ** 2 + second_complex_number.imag_part ** 2)
            return ComplexNumber(round(real_result,2), round(imag_result,2))
        except ZeroDivisionError as ex:
            raise ex

    def display_result_number_in_string(self):
        #Rectangular form:
        if self.imag_part < 0:
            operator = ""
            imag_char = "i"
        else:
            operator = "+"
            imag_char = "i"

        return "Rectangular form: {}{}{}{}\n{}".format(round(self.real_part, 6), operator, round(self.imag_part, 6),
                                                       imag_char, self.display_in_polar_form())

    def display_in_polar_form(self):
        # if self.real_part == 0:
        #TODO CHECK POLAR FORM for RLC module. Idea - new class RLC for RLC elements.
        #C has -90 phase. L has +90 phase
        if self.imag_part == 0 or self.real_part == 0:
            answer = "This number does not have polar form."
            # modulus = math.sqrt(self.real_part ** 2 + self.imag_part ** 2)
            # phase = 90
            # answer = "Polar form: {}∠{}°".format(round(modulus, 4), round(phase, 2))
        else:
            modulus = math.sqrt(self.real_part ** 2 + self.imag_part ** 2)
            phase = math.atan(self.imag_part / self.real_part) * 180 / math.pi
            answer = "Polar form: {}∠{}°".format(round(modulus, 4), round(phase, 2))

        return answer

