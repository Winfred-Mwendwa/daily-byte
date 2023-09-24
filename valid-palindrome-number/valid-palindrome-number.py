class Solution:
    def isPalindrome(self, x: int) -> bool:
        #negative numbers are not palindromic
        if x < 0:
            return False
        
        #multiple assignment
        original_x, reversed_x = x, 0

        while x > 0:
            last_digit = x % 10
            reversed_x = reversed_x * 10 + last_digit
            #remove last digit
            x //= 10
        return original_x == reversed_x