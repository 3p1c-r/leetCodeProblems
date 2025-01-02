# Given an integer n, return the smallest multiple of n that is divisible by 2.

def smallestEvenMultiple(n: int) -> int:
        for i in range(n,300):
            if i % n == 0 and i % 2 == 0: return i

print(smallestEvenMultiple(n=103))
