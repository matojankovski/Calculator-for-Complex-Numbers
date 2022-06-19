import re

class A:


    def __init__(self):
        self.re1 = 0
        self.re2 = 0
        self.scales = {
        "p": 0.000000000001,
        "n": 0.000000001,
        "u": 0.000001,
        "m": 0.001,
        "" :  1,
        "k": 1000,
        "M": 1000000,
        "G": 1000000000
    }

    def get(self):
        self.re1 = int(input())
        self.re2 = int(input())

    def print(self):
        print(self.re1 + self.re2)


class B(A):

    def minus(self):
        x = self.re1 - self.re2
        self.print()
        print(x)

    def GetValue(self):
        finalnumber = 0
        pattern = "^(\d*\.?\d*)([pmukgMG]*)"
        vstup = input()
        elementvalue = re.findall(pattern, vstup)
        number, unit = float(elementvalue[0][0]), elementvalue[0][1]
        finalnumber = round(number * self.scales[unit], 9)
        return finalnumber


if __name__ == '__main__':
    a = 5
    b = 5
    c = 0
    d = 0
    try:
        x = (a*c+b*d) / (c**2 + d**2)
        print(x)
    except ZeroDivisionError:
        print("ZERO DIVISION")

















    scales = {
        "p": 0.000000000001,
        "n": 0.000000001,
        "u": 0.000001,
        "m": 0.001,
        "k": 1000,
        "M": 1000000,
        "G": 1000000000
    }















    #
    #
    # result = input()
    # print(result)
    # resultinstring = ""
    # cislo_in_s = str(result).split(".")
    # if int(cislo_in_s[0]) > 0:
    #     digits = len(cislo_in_s[0]) - 1
    #     print(digits)
    #     if digits in range(1, 4):
    #         resultinstring = "{}.{}Ω".format(cislo_in_s[0], int(cislo_in_s[1]))
    #     elif digits in range(4, 7):
    #         prva_cast = int(cislo_in_s[0])//1000
    #         druha_cast = int(int(cislo_in_s[0]) % 1000/ 100)
    #         resultinstring  = "{}.{}{}Ω".format(prva_cast, druha_cast, "k" )
    #     elif digits in range(7, 10):
    #         prva_cast = round(int(cislo_in_s[0]) // 1000000)
    #         druha_cast = int(int(cislo_in_s[0]) % 1000000 / 10000)
    #         resultinstring = "{}.{}{}Ω".format(prva_cast, druha_cast, "M")
    #     elif digits in range(10, 13):
    #         prva_cast = round(int(cislo_in_s[0]) // 1000000000)
    #         druha_cast = int(int(cislo_in_s[0]) % 1000000000/ 10000000)
    #         resultinstring ="{}.{}{}Ω".format(prva_cast, druha_cast, "G")
    # elif int(cislo_in_s[0]) == 0:
    #     digits = len(cislo_in_s[1]) - 1
    #     if digits in range(1, 4):
    #         prva_cast = round(int(cislo_in_s[1]) // 1000)
    #         druha_cast = int((cislo_in_s[1]) % 1000) / 100
    #         resultinstring = "{}.{}{}Ω".format(prva_cast, druha_cast, "m")
    #     elif digits in range(4, 7):
    #         prva_cast = round(int(cislo_in_s[1]) // 1000000)
    #         druha_cast = int(int(cislo_in_s[1]) % 1000000 / 10000)
    #         resultinstring = "{}.{}{}Ω".format(prva_cast, druha_cast, "u")
    #     elif digits in range(7, 10):
    #         prva_cast = round(int(cislo_in_s[1]) // 1000000000)
    #         druha_cast = int(int(cislo_in_s[1]) % 1000000000 / 10000000)
    #         resultinstring = "{}.{}{}Ω".format(prva_cast, druha_cast, "n")
    #
    #
    #
    #
    #
    # print(cislo_in_s)
    # print(len(cislo_in_s[0]))
    # prva_cast = round(int(cislo_in_s[0])/int(scales["k"]))
    # druha_cast = int(cislo_in_s[0]) % int(scales["k"])
    # print(prva_cast)
    # print(druha_cast)
    # print("{}.{}{}Ω".format(prva_cast, druha_cast, "k" ))