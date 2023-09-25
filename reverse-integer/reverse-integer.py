class Solution:
    def reverse(self, x: int) -> int:

        #initialize negativity test flag to false
        isNegative = False
        if x < 0:
            isNegative = True #set flag to true if negative
            x = -x

        reversedNumber = 0

        while x:
            reversedNumber = reversedNumber * 10 + x % 10 #last digit
            x //= 10 #remove last digit
            #add bound check, do early return if met
            if reversedNumber >= 2 ** 31 - 1 or reversedNumber <= -2 ** 31:
                return 0

        return -reversedNumber if isNegative else reversedNumber