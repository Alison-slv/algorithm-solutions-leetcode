# 9.Palindrome Number
# easy


class Solution:
    def isPalindrome(self, x: int) -> bool:
        copyNumber = x
        reversedNumber = 0

        while x > 0:
            remainder = x % 10
            reversedNumber = reversedNumber * x + remainder
            x = x // 10

        if copyNumber == reversedNumber:
            print(f"{copyNumber} is an PALINDROME.")
            return True
        else:
            print(f"{copyNumber} is not a PALINDROME.")
            return False
