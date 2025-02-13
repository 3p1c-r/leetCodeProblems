def canPlaceFlowers(nums: list[int], n: int) -> bool:
        if n == 0: return True
        if n == 1 and len(nums) == 1 and nums[0] == 0: return True
        if n == len(nums): return False
        counter = 0
        index = -1
        for i in nums:
            index += 1
            if index == 0:
                if nums[1] == 0 and nums[0] == 0:
                    counter += 1
                    nums[0] = 1
            else:
                try:
                    if nums[index - 1] == 0 and nums[index + 1] == 0 and nums[index] == 0:
                        counter += 1
                        nums[index] = 1
                except:
                    pass
            if index + 1 == len(nums):
                if nums[index] == 0 and nums[index - 1] == 0:
                    counter += 1
                    nums[index] = 1
        if counter >= n: return True
        return False

print(canPlaceFlowers(nums=[1,0,0,0,1], n = 1))
print(canPlaceFlowers(nums=[1,0,0,0,1], n = 2))
