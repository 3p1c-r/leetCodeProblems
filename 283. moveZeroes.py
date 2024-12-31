#Move all zeroes to the end of the list, keeping the other numbers' order.

def moveZeroes(nums: list[int]) -> None:
        for i in nums:
            if i == 0:
                nums.append(nums.pop(nums.index(i)))

moveZeroes(nums=[0,1,0,12,0,3])
