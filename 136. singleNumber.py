#Given a list with multiple duplicate numbers and only one number appearing once in the list, return the singular number.

class Solution:
    def singleNumber(nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
            
    singleNumber(nums=[4,1,2,1,2])
