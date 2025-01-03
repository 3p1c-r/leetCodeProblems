# Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.


def numIdenticalPairs(nums: list[int]) -> int:
        counter = 0
        for i in range(0,len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j: counter += 1
        return counter

print(numIdenticalPairs(nums=[1,2,3,1,1,3]))
