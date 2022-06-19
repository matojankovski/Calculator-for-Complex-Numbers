

#NOT FINISHED RLC CALCULATOR
class RLC(Calculator):



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

