def thirdMax(nums: list[int]) -> int:
    if len(set(nums)) < 3: return(max(nums))
    else:
        x = max(nums)
        for i in nums:
            try: nums.remove(x)
            except: break    
        y = max(nums)
        for i in range(len(nums)):
            try: nums.remove(y)
            except: break
        return(max(nums))
print(thirdMax(nums=[3,3,3,3,4,3,2,3,3]))
