import re
import math

from ComplexNumber import ComplexNumber

SUBTRACT = "SUBTRACT"
ADD = "ADD"
MULTIPY = "MULTIPLY"
DIVIDE = "DIVIDE"

COMPLEXNUMBERPATTERN = "^(?=[iIjJ.\d+-])([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[+-]?\d+)?(?![iIjJ.\d]))?([+-]?(?:(?:\d+(?:\.\d*)?|\.\d+)(?:[+-]?\d+)?)?[iIjJ])?$"


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



class Calculator:


    def __init__(self):
        self.realResult = 0
        self.imgResult = 0
        self.operation = "+"
        self.first_complex_number = None
        self.second_complex_number = None
        self.result_in_string = "real + imgi"
        self.frequency = 0
        self.pi = math.pi
        self.value = 0
        self.modulus = 0
        self.phase = 0



    



    def GetComplexNumber(self):
        while True:
            number = input()
            try:
                return ComplexNumber.ParseComplexNumer(number)
            except AttributeError as ex:
                print("Wrong input")
                continue


    def GetOperation(self):
        while True:
            operation = input()
            try:
                if operation == "+":
                    self.operation = ADD
                    break
                elif operation == "-":
                    self.operation = SUBTRACT
                    break
                elif operation == "*":
                    self.operation = MULTIPY
                    break
                elif operation == "/":
                    self.operation = DIVIDE
                    break
            except AttributeError as ex:
                print("Wrong input")
                continue

    def DefineOperation(self):
        print("Enter 1st complex number:")
        self.first_complex_number= self.GetComplexNumber()
        print("Enter operation:")
        self.GetOperation()
        print("Enter 2nd complex number:")
        self.second_complex_number = self.GetComplexNumber()

    def AddComplexNumbers(self):
        return self.first_complex_number.Add(self.second_complex_number)

    def SubtrackComplexNumbers(self):
        return self.first_complex_number.Subtract(self.second_complex_number)

    def MultiplyComplexNumbers(self):
        return self.first_complex_number.Multiply(self.second_complex_number)

    def DivideComplexNumbers(self):
        try:
            return self.first_complex_number.Divide(self.second_complex_number)
        except ZeroDivisionError as ex:
            print("Division by Zero!")

    def GivePolarForm(self):
        if self.operation == ADD:
            print()



    # def DivideComplexNumbers(self):
    #     try:
    #         self.realResult = (self.first_complex_number.real_part * self.second_complex_number.real_part + self.first_complex_number.imag_part * self.second_complex_number.imag_part) / (self.second_complex_number.real_part*self.second_complex_number.real_part + self.second_complex_number.imag_part*self.second_complex_number.imag_part)
    #         self.imgResult = (self.first_complex_number.imag_part*self.second_complex_number.real_part - self.first_complex_number.real_part*self.second_complex_number.imag_part) / (self.second_complex_number.real_part*self.second_complex_number.real_part + self.second_complex_number.imag_part*self.second_complex_number.imag_part)
    #         result = [round(self.realResult, 3), round(self.imgResult, 3)]
    #         return result
    #     except ZeroDivisionError as ex:
    #         print ("Division by Zero!")
    #         continue
    #




    # def DisplayResultNumberInString(self):
    #     if self.imgResult < 0:
    #         operator = ""
    #         imag_char = "i"
    #     else:
    #         operator = "+"
    #         imag_char = "i"
    #
    #     return "Rectangular form : {}{}{}{}".format(round(self.realResult,2), operator, round(self.imgResult,2), imag_char)

    # def DisplayInPolarForm(self):
    #     # self.GetPolarForm()
    #     answer = "Polar form : {}∠{}°".format(round(self.modulus,2), round(self.phase,2))
    #     return answer
    #
    #
    #
    # def GetPolarForm(self):
    #     try:
    #         self.modulus= round(math.sqrt(self.realResult**2 + self.imgResult**2 ), 2)
    #         self.phase = math.atan(self.imgResult/self.realResult)*180/self.pi
    #         return self.modulus, round(self.phase,2)
    #     except ZeroDivisionError:
    #         message = "Division by Zero Error"
    #         return message



    def Compute(self):
        while True:
            self.DefineOperation()
            if self.operation == ADD:
                print(self.AddComplexNumbers())
            elif self.operation == SUBTRACT:
                print(self.SubtrackComplexNumbers())
            elif self.operation == DIVIDE:
                print(self.DivideComplexNumbers())
            elif self.operation == MULTIPY:
                print(self.MultiplyComplexNumbers())




class RLC(Calculator):

    def ChooseElement(self):
        print("Choose R, L or C")
        element = ""
        while True:
            vstup = input()
            if vstup == "R":
                element = "R"
                break
            elif vstup == "L":
                element = "L"
                break
            elif vstup == "C":
                element = "C"
                break
            else:
                print("Wrong input")
                continue
        return element

    def GetValue(self):
        finalnumber = 0
        pattern = "^(\d*\.?\d*)([pmukgMG]*)"
        while True:
            vstup = input()
            elementvalue = re.findall(pattern, vstup)
            if elementvalue:
                number, unit = float(elementvalue[0][0]), elementvalue[0][1]
                finalnumber = round(number * self.scales[unit], 9)
                break
            else:
                print("Wrong input")
                continue
        return finalnumber


    def GetValueAndFrequency(self):
        print("Insert value")
        self.value = self.GetValue()
        print("Insert frequency")
        self.frequency = self.GetValue()

    def GetZofCapacitor(self):
        self.GetValueAndFrequency()
        while True:
            try:
                ZofCapacitor = round(1 / (2* self.pi * self.frequency * self.value), 8)
                return 0, -ZofCapacitor
            except ZeroDivisionError:
                message = "Division by Zero. Enter correct values!"
                return message


    def GetZofInductor(self):
        self.GetValueAndFrequency()
        ZofInductor = round(2 * self.pi * self.frequency * self.value, 8)
        return 0, ZofInductor

    def GetZofResistor(self):
        print("Insert resistance")
        Rimpedance = round(self.GetValue(), 8)
        return Rimpedance, 0

    def GetImpedanceOfSeriesConnection(self):
        result = self.AddComplexNumbers()
        print(result)

    def GetImpedanceOfParallelConnection(self):
        result = self.AddComplexNumbers()
        print(result)



    def DisplayResultInSIValues(self):
        if self.imgResult < 0:
            operator = ""
            imag_char = "i"
        else:
            operator = "+"
            imag_char = "i"

        return "{}{}{}{}".format(self.realResult, operator, self.imgResult, imag_char, "")

    def ChangeToAdmitance(self):
        try:
            self.first_complex_number.real_part = 1 / self.first_complex_number.real_part
        except ZeroDivisionError:
            self.first_complex_number.real_part = 0
        try:
            self.first_complex_number.imag_part = 1 / self.first_complex_number.imag_part
        except ZeroDivisionError:
            self.first_complex_number.imag_part = 0
        try:
            self.second_complex_number.real_part = 1 / self.second_complex_number.real_part
        except ZeroDivisionError:
            self.second_complex_number.real_part = 0
        try:
            self.second_complex_number.imag_part = 1 / self.second_complex_number.imag_part
        except ZeroDivisionError:
            self.second_complex_number.imag_part = 0






    def Calculate(self):
        while True:
            elementone = self.ChooseElement()
            if elementone == "R":
                self.first_complex_number.real_part, self.first_complex_number.imag_part = self.GetZofResistor()
            elif elementone == "C":
                self.first_complex_number.real_part, self.second_complex_number.imag_part = self.GetZofCapacitor()
            elif elementone == "L":
                self.first_complex_number.real_part, self.first_complex_number.imag_part = self.GetZofInductor()
            print("Choose 2nd element:")
            elementtwo = self.ChooseElement()
            if elementtwo == "R":
                self.second_complex_number.real_part, self.second_complex_number.imag_part = self.GetZofResistor()
            elif elementtwo == "C":
                self.second_complex_number.real_part, self.second_complex_number.imag_part = self.GetZofCapacitor()
            elif elementtwo == "L":
                self.second_complex_number.real_part, self.second_complex_number.imag_part = self.GetZofInductor()
            connection = self.ChooseSPconnection()
            if connection == "S":
                self.GetImpedanceOfSeriesConnection()
                totalZ, phase = self.GetPolarForm()
                print(totalZ, phase)
            elif connection == "P":
                self.ChangeToAdmitance()
                self.GetImpedanceOfParallelConnection()
                totalZ, phase = self.GetPolarForm()
                print(totalZ, phase)


    def ChooseSPconnection(self):
        print("Choose S for series or P for parallel connection of elements")
        connection = ""
        while True:
            vstup = input()
            if vstup == "S":
                connection = "S"
                break
            elif vstup == "P":
                connection = "P"
                break
            else:
                print("Wrong input")
                continue
        return connection


    def GetInPolarForm(self):
        modulus, angle = self.GetPolarForm()
        resultinpolarform = "{}Ω ∠{}°".format(modulus, angle)
        return resultinpolarform





    def WriteInString(self, result):
        resultinstring = ""
        resultparsed = str(result).split(".")
        if int(resultparsed[0]) > 0:
            digits = len(resultparsed[0]) - 1
            print(digits)
            if digits in range(1, 4):
                resultinstring = "{}.{}Ω".format(resultparsed[0], int(resultparsed[1]))
            elif digits in range(4, 7):
                firstpart = int(resultparsed[0]) // 1000
                secondpaart = int(int(resultparsed[0]) % 1000 / 100)
                resultinstring = "{}.{}{}Ω".format(firstpart, secondpaart, "k")
            elif digits in range(7, 10):
                firstpart = round(int(resultparsed[0]) // 1000000)
                secondpaart = int(int(resultparsed[0]) % 1000000 / 10000)
                resultinstring = "{}.{}{}Ω".format(firstpart, secondpaart, "M")
            elif digits in range(10, 13):
                firstpart = round(int(resultparsed[0]) // 1000000000)
                secondpaart = int(int(resultparsed[0]) % 1000000000 / 10000000)
                resultinstring = "{}.{}{}Ω".format(firstpart, secondpaart, "G")
        elif int(resultparsed[0]) == 0:
            digits = len(resultparsed[1]) - 1
            if digits in range(1, 4):
                firstpart = round(int(resultparsed[1]) // 1000)
                secondpaart = int((resultparsed[1]) % 1000) / 100
                resultinstring = "{}.{}{}Ω".format(firstpart, secondpaart, "m")
            elif digits in range(4, 7):
                firstpart = round(int(resultparsed[1]) // 1000000)
                secondpaart = int(int(resultparsed[1]) % 1000000 / 10000)
                resultinstring = "{}.{}{}Ω".format(firstpart, secondpaart, "u")
            elif digits in range(7, 10):
                firstpart = round(int(resultparsed[1]) // 1000000000)
                secondpaart = int(int(resultparsed[1]) % 1000000000 / 10000000)
                resultinstring = "{}.{}{}Ω".format(firstpart, secondpaart, "n")

        return resultinstring




















if __name__ == '__main__':
    print("Enter which type of calculator to initiate. Enter 'COMPLEX' for basic operations with complex numbers. Enter 'RLC' for calculator for impedance of R, L or C elements.")

    while True:
        vstup = input()
        if vstup == "COMPLEX":
            kalkulacka = Calculator()
            kalkulacka.Compute()
            break
        elif vstup == "RLC":
            kalkulacka = RLC()
            kalkulacka.Calculate()
            break
        else:
            print("Enter valid statement.")
            continue





