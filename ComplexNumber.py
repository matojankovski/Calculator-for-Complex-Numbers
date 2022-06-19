import math
import re

COMPLEXNUMBERPATTERN = "^(?=[iIjJ.\d+-])([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[+-]?\d+)?(?![iIjJ.\d]))?([+-]?(?:(?:\d+(?:\.\d*)?|\.\d+)(?:[+-]?\d+)?)?[iIjJ])?$"
VALUEOFELEMENT = "^(\d*\.?\d*)([pmukgMG]*)"

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
        return self.DisplayResultNumberInString()


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

    def Add(self, secondcomplexnumber):
        realresult = self.real_part + secondcomplexnumber.real_part
        imagresult = self.imag_part + secondcomplexnumber.imag_part

        return ComplexNumber(realresult, imagresult)

    def Subtract(self, secondcomplexnumber):
        realresult = self.real_part - secondcomplexnumber.real_part
        imagresult = self.imag_part - secondcomplexnumber.imag_part

        return ComplexNumber(realresult, imagresult)

    def Multiply(self, secondcomplexnumber):
        realresult = (self.real_part * secondcomplexnumber.real_part ) - (self.imag_part * secondcomplexnumber.imag_part)
        imagresult = (self.real_part * secondcomplexnumber.imag_part) + (self.imag_part * secondcomplexnumber.real_part)

        return ComplexNumber(realresult, imagresult)

    def Divide(self, secondcomplexnumber):
        try:
            realresult = (self.real_part * secondcomplexnumber.real_part + self.imag_part * secondcomplexnumber.imag_part)/ (secondcomplexnumber.real_part**2 + secondcomplexnumber.imag_part**2)
            imagresult = (self.imag_part * secondcomplexnumber.real_part - self.real_part*secondcomplexnumber.imag_part)/ (secondcomplexnumber.real_part**2 + secondcomplexnumber.imag_part**2)
            return ComplexNumber(realresult, imagresult)
        except ZeroDivisionError as ex:
            raise ex


    # def DisplayResultNumberInString(self):
    #     if self.imag_part < 0:
    #         operator = ""
    #         imag_char = "i"
    #     else:
    #         operator = "+"
    #         imag_char = "i"
    #
    #     return "Rectangular form: {}{}{}{}".format(round(self.real_part, 2), operator, round(self.imag_part, 2),
    #                                                 imag_char)


    def DisplayResultNumberInString(self):
        #Rectangular form:
        if self.imag_part < 0:
            operator = ""
            imag_char = "i"
        else:
            operator = "+"
            imag_char = "i"

        return "Rectangular form: {}{}{}{}\n{}".format(round(self.real_part, 2), operator, round(self.imag_part, 2),
                                                         imag_char, self.DisplayInPolarForm())


    def DisplayInPolarForm(self):
        try:
            modulus = round(math.sqrt(self.real_part ** 2 + self.imag_part ** 2), 2)
            phase = math.atan(self.imag_part / self.real_part) * 180 / math.pi
            answer = "Polar form : {}∠{}°".format(round(modulus, 2), round(phase, 2))
        except ZeroDivisionError:
            answer = "This number doesn't have a polar form."
        return answer


    @staticmethod
    def ParseValue(inputelement):
        value = re.findall(VALUEOFELEMENT, inputelement)
        if not value:
            raise AttributeError("COULD NOT PARSE COMPLEX NUMBER")
        number, unit = float(value[0][0]), value[0][1]
        finalnumber = round(number * scales[unit], 9)

        return finalnumber

