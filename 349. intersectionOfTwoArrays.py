#given two arrays, return an array of their intersection (elements present in both arrays)

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for i in nums1:
            if i in nums2 and i not in result: result.append(i)

        return result

print(intersection(nums1= [4,9,5], nums2= [9,4,9,8,4]))
