#Check if a string ransomNote can be constructed with the letters from a string magazine.

def canConstruct(ransomNote: str, magazine: str) -> bool:
        counter = 0
        for i in ransomNote:
            if ransomNote.count(i) <= magazine.count(i): counter += 1
        if counter == len(ransomNote): return True
        return False

print(canConstruct(ransomNote="fihjjjjei", magazine="hjibagacbhadfaefdjaeaebgi"))
