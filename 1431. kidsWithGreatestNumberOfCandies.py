#Given a list representing the number of candies that a few kids have and an integer extraCandies, return a boolean array that shows whether each kid will have the greatest number of candies in the group after giving them extraCandies.


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
        boolArray = []
        for i in candies:
            if i + extraCandies >= max(candies):boolArray.append(True)
            else: boolArray.append(False)
        return boolArray

print(kidsWithCandies(candies=[2,3,5,1,3], extraCandies=3))
