class Solution:
    def mySqrt(self, x: int) -> int:
        #USING BINARY SEARCH time: O(log(x)), space O(1)
        if x == 1:
            return 1
        left, right = 1, x #sqrt for any no. greater than 1 is at least 1

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
        