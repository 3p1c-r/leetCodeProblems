#Given a number, return the sum of its digits if it is a Harshad number, otherwise return -1.

def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
        list1 = []
        for i in str(x):
            list1.append(int(i))
        if x % sum(list1) == 0: return(sum(list1))
        else: return -1

print(sumOfTheDigitsOfHarshadNumber(x=18))
