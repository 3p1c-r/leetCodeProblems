#Return the permutation difference of two strings. The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.


def findPermutationDifference(s: str, t: str) -> int:
        lst = []
        for i in s:
            lst.append(abs(s.index(i)-t.index(i)))
        return sum(lst)

print(findPermutationDifference(s="abc", t="bac"))
