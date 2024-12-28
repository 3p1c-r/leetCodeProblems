#Check if two strings are isomorphic

def isIsomorphic(s: str, t: str) -> bool:
        myDict = {}
        invDict = {}
        for i in range(len(s)):
            if s[i] not in myDict and t[i] in invDict:
                return False
            if s[i] in myDict and myDict[s[i]] != t[i]:
                return False
            myDict[s[i]] = t[i]
            invDict[t[i]] = s[i]

isIsomorphic(s="egg",t="add")
