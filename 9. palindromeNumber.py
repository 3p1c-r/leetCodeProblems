#Check if a number is a palindrome(a word or number typed the same way backwards)

class Solution:
    def isPalindrome(x: int) -> bool:
        arr = []
        for i in str(x):
            arr.append(i)
        arr2 = "".join(arr)
        arreverse = arr.copy()
        arreverse.reverse()
        arreverse2 = "".join(arreverse)
        
        if arreverse2 == arr2:
            print(True)
            return True
        else:
            print(False)
            return False

    isPalindrome(x=121)
    isPalindrome(x=123)

        
