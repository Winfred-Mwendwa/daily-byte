class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        #binary exponentiation: 
            #         1   n=0
            # x^n =  (x^n-1/2)^2 * x  n odd
            #        (x^n/2)^2 n even
        while n > 0:
            #multiply x into result for odd powers
            if n % 2 != 0:
                result *= x

            x *= x  # Square x
            #perform floor division of n by 2 to half the exponent for next iteration
            n //= 2

        return result