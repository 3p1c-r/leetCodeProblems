#Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where answer[0] is a list of all distinct integers in nums1 which are not present in nums2 and answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[],[]]
        for i in nums1:
            if i not in nums2 and i not in answer[0]: answer[0].append(i)
        for i in nums2:
            if i not in nums1 and i not in answer[1]: answer[1].append(i)
        return answer

print(findDifference(nums1=[1,2,3],nums2=[2,4,6])
