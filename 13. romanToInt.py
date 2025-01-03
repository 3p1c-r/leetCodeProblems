#Given a string of roman numerals, convert the roman numerals to an integer.

def romanToInt(s: str) -> int:
        counter = 0
        myDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        s = s.replace("IV","IIII")
        s = s.replace("IX","VIIII")
        s = s.replace("XL","XXXX")
        s = s.replace("XC","LXXXX")
        s = s.replace("CD","CCCC")
        s = s.replace("CM","DCCCC")
        for i in s:
            counter += myDict[i]
        return counter

print(romanToInt(s="MCMXCIV"))
