def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for i in nums1:
            if i in nums2: 
                result.append(i)
                nums2.remove(i)

        return result

print(intersect(nums1= [1,2,2,1], nums2= [2,2]))
