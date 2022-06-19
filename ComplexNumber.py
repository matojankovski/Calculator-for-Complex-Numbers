import re

COMPLEXNUMBERPATTERN = "^(?=[iIjJ.\d+-])([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[+-]?\d+)?(?![iIjJ.\d]))?([+-]?(?:(?:\d+(?:\.\d*)?|\.\d+)(?:[+-]?\d+)?)?[iIjJ])?$"


class ComplexNumber:
    def __init__(self, real_part, imag_part):
        self.real_part = real_part
        self.imag_part = imag_part

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real_part == other.real_part and self.imag_part == other.imag_part
        return False

    @staticmethod
    def ParseComplexNumer(complexnumber):
        complex_number = re.findall(COMPLEXNUMBERPATTERN, complexnumber)
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
