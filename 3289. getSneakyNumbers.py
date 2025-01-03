#Return the two sneaky numbers which appear more than once in a list nums.

def getSneakyNumbers(nums: list[int]) -> list[int]:
        twoNums = []
        for i in nums:
            if nums.count(i) != 1 and i not in twoNums: twoNums.append(i)
        return twoNums

print(getSneakyNumbers(nums=[0,1,1,0]))
