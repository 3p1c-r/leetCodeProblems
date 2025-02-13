def isValid(word: str) -> bool:
        counter = 0
        vowelstr = "aeiouAEIOU"
        x = False
        if len(word)>=3: x = True
        for i in word:
            if i.isdigit() == True: word = word.replace(i,"")
        for i in word:
            if i not in vowelstr: counter +=1
        if counter == len(word): return False
            
        for i in word:
            if i in vowelstr: word = word.replace(i,"")
        if word.isalnum() and x: return True
        return False
print(isValid(word="234Adas"))
