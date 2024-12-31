#Given two lists, merge their numbers and sort them, removing n zeroes from the first list.

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        while 0 in nums1 and n != 0:
            nums1.remove(0)
            n-=1
        print(nums1)

merge(nums1=[1,2,3,0,0,0],m=3,nums2 = [2,5,6], n = 3)
