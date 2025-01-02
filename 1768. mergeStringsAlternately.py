#Given two strings word1 and word2, merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

def mergeAlternately(word1: str, word2: str) -> str:
        strList = []
        count1 = 0
        count2 = 0
        for i in range(len(word1) + len(word2)):
            if count1 == len(word1):
                try: strList.append(word2[i])
                except: pass
            elif count2 == len(word2):
                try: strList.append(word1[i])
                except: pass
            else:
                strList.append(word1[i])
                count1 += 1
                strList.append(word2[i])
                count2 += 1
        strFinal = "".join(strList)
        return strFinal


print(mergeAlternately(word1="ab",word2="pqrs"))
