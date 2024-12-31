#Given a string, return the length of the last word in the string.
 
 def lengthOfLastWord(self, s: str) -> int:
        lastWordArray = []
        counter = 0
        nonSpaceLetteraEncountered = False
        
        for i in reversed(s):
            counter += 1
            if i == " ":
                print("blank found")
                if nonSpaceLetteraEncountered == True:
                    print("breaking")
                    return len(lastWordArray)
                
            else:
                lastWordArray.append(i)
                print("i is not blank, letter: ", i, ", ", lastWordArray.index(i))
                nonSpaceLetteraEncountered = True
                if counter == len(s):
                    return len(lastWordArray)
