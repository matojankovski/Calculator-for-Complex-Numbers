import re
import math

from ComplexNumber import ComplexNumber

SUBTRACT = "SUBTRACT"
ADD = "ADD"
MULTIPY = "MULTIPLY"
DIVIDE = "DIVIDE"
COMPLEX = "COMPLEX"
RLC = "RLC"

class Calculator:


    def __init__(self):
        self.realResult = 0
        self.imgResult = 0
        self.operation = "+"
        self.first_complex_number = None
        self.second_complex_number = None
        self.result_in_string = "real + imgi"
        self.pi = math.pi


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



    def ComputeComplexNumber(self):
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
            self.QuitProgram()

    def QuitProgram(self):
        print("Enter 'y' to abort the program")
        vstup = input()
        if vstup == "y":
            quit()
        else:
            pass





if __name__ == '__main__':
    calculator = Calculator()
    calculator.ComputeComplexNumber()





