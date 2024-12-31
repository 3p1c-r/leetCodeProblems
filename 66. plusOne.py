class Solution:
    def plusOne(digits: list[int]) -> List[int]:
        digits2 = [str(x) for x in digits]
        digitstring = "".join(digits2)
        digitinteger = int(digitstring)
        digitinteger += 1
        digitstring2 = str(digitinteger)
        digits.clear()
        for i in digitstring2:
            digits.append(int(i))
        print(digits)
        return digits

    plusOne(digits=[1,2,3])
    
        
