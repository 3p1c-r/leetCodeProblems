#Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

def addStrings(num1: str, num2: str) -> str:
        import sys
        #this line sets the maximum amount of digits in a string to 6000, allowing for some testcases to be passed.
        sys.set_int_max_str_digits(6000)
        expressionList = [num1, "+", num2]
        numExpression = "".join(expressionList)
        return str(eval(numExpression))
  
