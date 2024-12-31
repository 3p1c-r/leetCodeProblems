#Return True if s is an anagram of t, otherwise return False.

def isAnagram(s: str, t: str) -> bool:
        print(sorted(s) == sorted(t))
        return sorted(s) == sorted(t)
isAnagram(s="rat",t="car")
