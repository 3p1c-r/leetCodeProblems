#Given a string, return a string with the order of the words in the original string reversed.

def reverseWords(s: str) -> str:
        lst = s.split()
        return " ".join(reversed(lst))

print(reverseWords(s="the sky is blue"))
