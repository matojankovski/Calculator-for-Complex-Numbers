import re
import math

from ComplexNumber import ComplexNumber

SUBTRACT = "SUBTRACT"
ADD = "ADD"
MULTIPY = "MULTIPLY"
DIVIDE = "DIVIDE"
R = "R"
C = "C"
L = "L"
SERIES = "S"
PARALLEL = "P"
RESISTANCE = "RESISTANCE"
CAPACITANCE = "CAPACITANCE"
INDUCTANCE = "INDUCTANCE"
COMPLEX = "COMPLEX"
RLC = "RLC"


class Calculator:


    def __init__(self):
        # self.realResult = 0
        # self.imgResult = 0
        self.operation = "+"
        self.first_complex_number = None
        self.second_complex_number = None
        self.result_in_string = "real + imgi"
        self.pi = math.pi
        self.element_1 = "R"
        self.element2 = "R"
        self.unit = "resistance"
        self.connection = "Series"
        self.parallel_numerator_number1 = None
        self.parallel_denominator_number2 = None

    def define_type_of_calculator(self):
        print("Define type of calculator. Type COMPLEX or RLC")
        while True:
            type_of_calculator = input()
            try:
                if type_of_calculator == COMPLEX:
                    self.compute_complex_number()
                    break
                elif type_of_calculator == RLC:
                    self.get_impedance_of_two_elements()
                    break
            except AttributeError as ex:
                print("Wrong input")
                continue


    def get_complex_number(self):
        while True:
            number = input()
            try:
                return ComplexNumber.parse_complex_numer(number)
            except AttributeError as ex:
                print("Wrong input")
                continue

    def get_value_of_element(self):
        while True:
            number_1= input()
            try:
                value = ComplexNumber.parse_value(number_1)
                break
            except AttributeError as ex:
                print("Wrong input")
        return value

    def get_operation(self):
        while True:
            operation = input()
            try:
                self.operation = ComplexNumber.get_sign_for_operation(operation)
                return self.operation
            except AttributeError as ex:
                print("Wrong input")

    def define_operation(self):
        print("Enter 1st complex number:")
        self.first_complex_number= self.get_complex_number()
        print("Enter operation:")
        self.get_operation()
        print("Enter 2nd complex number:")
        self.second_complex_number = self.get_complex_number()

    def add_complex_numbers(self):
        return self.first_complex_number.add(self.second_complex_number)

    def subtrack_complex_numbers(self):
        return self.first_complex_number.subtract(self.second_complex_number)

    def multiply_complex_numbers(self):
        return self.first_complex_number.multiply(self.second_complex_number)

    def divide_complex_numbers(self):
        try:
            return self.first_complex_number.divide(self.second_complex_number)
        except ZeroDivisionError as ex:
            print("Division by Zero!")

    def parallel_connection(self):
        self.parallel_numerator_number1 = self.multiply_complex_numbers()
        self.parallel_denominator_number2 = self.add_complex_numbers()

        return self.parallel_numerator_number1.divide(self.parallel_denominator_number2)

    #TODO - improve function. Divide into two functions - one in Class ComplexNumber as static. Second here to allow
    #easier testing of user input
    def define_element(self):
        print("Define element: R, L or C")
        while True:
            vstup = input()
            try:
                if vstup == "R":
                    return R, RESISTANCE
                elif vstup == "C":
                    return C, CAPACITANCE
                elif vstup == "L":
                    return L, INDUCTANCE
            except AttributeError as ex:
                print("Wrong input")
                continue

    # TODO - improve function. Divide into two functions - one in Class ComplexNumber as static. Second here to allow
    # easier testing of user input
    def define_connection(self):
        print("Define connection: S for series or P for parallel")
        while True:
            vstup = input()
            try:
                if vstup == "S":
                    self.connection = SERIES
                    break
                elif vstup == "P":
                    self.connection = PARALLEL
                    break
            except AttributeError as ex:
                print("Wrong input")
                continue

    #TODO - make this more simple.
    def get_impedance_of_two_elements(self):
        self.define_connection()
        self.element_1, self.unit = self.define_element()
        #SERIEC CONNECTION - ZR = R, ZL =0 + 2*pi*L*f, ZC = 0 + 1/2*pi*L*f
        #for series connection : Z = ZR+ZL+ZC (example)
        #USING GetADmitance for C to get 1/2*pi*L*f
        #USING GetImpedance for R, L to get according to the equations
        if self.connection == SERIES:
            if self.element_1 == C:
                print("Enter {} of element {}".format(self.unit, self.element_1))
                value_1 = self.get_value_of_element()
                print("Enter operating frequency of element {}".format(self.element_1))
                frequency = self.get_value_of_element()
                self.first_complex_number = ComplexNumber.get_admitance(-value_1, frequency)
            else:
                print("Enter {} of element {}".format(self.unit, self.element_1))
                value_1 = self.get_value_of_element()
                print("Enter operating frequency of element {}".format(self.element_1))
                frequency = self.get_value_of_element()
                self.first_complex_number = ComplexNumber.get_impedance(value_1, frequency)
            print(self.first_complex_number)
            self.element2, self.unit = self.define_element()
            if self.element2 == C:
                print("Enter {} of element {}".format(self.unit, self.element2))
                value2 = self.get_value_of_element()
                print("Enter operating frequency of element {}".format(self.element2))
                frequency = self.get_value_of_element()
                self.second_complex_number = ComplexNumber.get_admitance(-value2, frequency)
            else:
                print("Enter {} of element {}".format(self.unit, self.element2))
                value2 = self.get_value_of_element()
                print("Enter operating frequency of element {}".format(self.element2))
                frequency = self.get_value_of_element()
                self.second_complex_number = ComplexNumber.get_impedance(value2, frequency)
            print(self.second_complex_number)
            print("Impedance of {} and {} in {} connection is:\n".format(self.element_1, self.element2, self.connection), str(self.add_complex_numbers()), "")
        #ZR = R, ZL =0 + 2*pi*L*f, ZC = 0 + 1/2*pi*L*f
        # for parallel connection : 1/Z = 1/ZR+1/ZL+1/ZC (example)
        # USING GetImpedance for C to get 1/2*pi*L*f
        # USING GetADmitance for R, L to get according to the equations
        elif self.connection == PARALLEL:
            if self.element_1 == C:
                print("Enter {} of element {}".format(self.unit, self.element_1))
                value_1 = self.get_value_of_element()
                print("Enter operating frequency of element {}".format(self.element_1))
                frequency = self.get_value_of_element()
                self.first_complex_number = ComplexNumber.get_admitance(-value_1, frequency)
            else:
                print("Enter {} of element {}".format(self.unit, self.element_1))
                value_1 = self.get_value_of_element()
                print("Enter operating frequency of element {}".format(self.element_1))
                frequency = self.get_value_of_element()
                self.first_complex_number = ComplexNumber.get_impedance(value_1, frequency)
            self.element2, self.unit = self.define_element()
            if self.element2 == C:
                print("Enter {} of element {}".format(self.unit, self.element2))
                value2 = self.get_value_of_element()
                print("Enter operating frequency of element {}".format(self.element2))
                frequency = self.get_value_of_element()
                self.second_complex_number = ComplexNumber.get_admitance(-value2, frequency)
            else:
                print("Enter {} of element {}".format(self.unit, self.element2))
                value2 = self.get_value_of_element()
                print("Enter operating frequency of element {}".format(self.element2))
                frequency = self.get_value_of_element()
                self.second_complex_number = ComplexNumber.get_impedance(value2, frequency)
            print("Impedance of {} and {} in {} connection is:\n".format(self.element_1, self.element2, self.connection), str(self.parallel_connection()))
            self.quit_program()

    def compute_complex_number(self):
        while True:
            self.define_operation()
            if self.operation == ADD:
                print(self.add_complex_numbers())
            elif self.operation == SUBTRACT:
                print(self.subtrack_complex_numbers())
            elif self.operation == DIVIDE:
                print(self.divide_complex_numbers())
            elif self.operation == MULTIPY:
                print(self.multiply_complex_numbers())
            self.quit_program()

    def quit_program(self):
        print("Enter 'y' to abort the program")
        vstup = input()
        if vstup == "y":
            quit()
        else:
            pass


if __name__ == '__main__':
    calculator = Calculator()
    calculator.define_type_of_calculator()





