import re

class RLCLogic():



    def __init__(self):
        self.element1 = 0
        self.element2 = 0
        self.frequency = 0
        self.pi = 3.14
        self.re1 = 0
        self.re2 = 0
        self.img1 = 0
        self.img2 = 0

        self.scales = {
        "p": 0.000000000001,
        "n": 0.000000001,
        "u": 0.000001,
        "m": 0.001,
        "k": 1000,
        "M": 1000000,
        "G": 1000000000
    }


    def ChooseElement(self):
        print("Choose R, L or C")
        vstup = input()
        if vstup == "R":
            return "Resistor"
        elif vstup == "L":
            return "Inductor"
        elif vstup == "C":
            return "Capacitor"

    def GetValue(self):
        finalnumber = 0
        pattern = "(\d+(?:\.\d*)?)([pnumkMG])|\d+(?:\.\d*)?"
        vstup = input()
        elementvalue = re.findall(pattern, vstup)
        # print(elementvalue)
        number, unit = float(elementvalue[0][0]), elementvalue[0][1]
        finalnumber = number * self.scales[unit]
        return finalnumber

    def GetFrequency(self):
        print("Insert frequency")
        self.frequency = self.GetValue()


    def GetValueOfElement(self):
        valueofelement = self.GetValue()
        return 2*self.pi * self.frequency * valueofelement

    def InvertValueOfElement(self, admitance):
        return 1 / admitance

    def GetZofCapacitor(self):
        print("Insert capacitance")
        capacitance = self.GetValue()
        print("Insert frequency")
        self.GetFrequency()
        ZofCapacitor = 1 / (self.pi * self.frequency * capacitance)
        return 0, ZofCapacitor


    def GetZofInductor(self):
        print("Insert inductance")
        inductance = self.GetValue()
        print("Insert frequency")
        self.GetFrequency()
        ZofInductor = 2 * self.pi * self.frequency * inductance
        return 0, ZofInductor

    def GetZofRessistor(self):
        Rimpedance = self.GetValue()
        return Rimpedance

    def Compute(self):
        while True:
            element = self.ChooseElement()
            if element == "Resistor":
                print("Insert resistance")
                value = self.GetValue()
                break
            elif element == "Capacitor":
                value = self.GetZofCapacitor()
                break
            elif element == "Inductor":
                value, f = self.GetZofInductor()
                break
            print("WRONG INPUT")
            continue
        print(value)
        # if f is not None:
        #     print(f)

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
















if __name__ == '__main__':
    elektrokalkulacla = RLCLogic()
    elektrokalkulacla.Compute()



