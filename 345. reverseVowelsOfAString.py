def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowelList = []
        for i in s:
            if i in vowels: 
                vowelList.append(i)
                s = s.replace(i, "_", 1 )
        vowelList.reverse()
        for i in s:
            if i == "_":
                s = s.replace(i,vowelList[0],1)
                vowelList.pop(0)
        return s

print(reverseVowels(s="icecream"))
