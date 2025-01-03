#You are given positive integers n and m. Define two integers as follows: num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m. num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m. Return the integer num1 - num2.

def differenceOfSums(n: int, m: int) -> int:
        lst1 = []
        lst2 = []

        for i in range(1,n+1):
            if i % m != 0: lst1.append(i)
            else: lst2.append(i)
        return sum(lst1) - sum(lst2)

print(differenceOfSums(n=10,m=3))
