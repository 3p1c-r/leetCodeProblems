#Check if a string is a palindrome after removing all non-alphanumeric characters and changing every uppercase letter to lowercase.

def isPalindrome(s: str) -> bool:
        s2 = ''.join(char for char in s if char.isalnum()).lower()
        if s2[::-1] == s2: 
            return True
        return False

isPalindrome(s="A man, a plan, a canal: Panama")
