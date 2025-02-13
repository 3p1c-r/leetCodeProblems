def detectCapitalUse(word: str) -> bool:
        if word.isupper() == True or word[0].isupper() == True and word[1:].islower() == True or word.islower() == True: return True
        return False

print(detectCapitalUse(word = "Leetcode"))
print(detectCapitalUse(word = "USA"))
print(detectCapitalUse(word = "LeetcoCde"))
