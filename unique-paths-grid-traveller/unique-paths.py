class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        # m-rows, n-cols
        #uniquePaths(2,3)
        #base cases
        #brute force; time: O(2^m*n) space:O(n)
        #optimal; memoization; O(m*n) space: O(m*n)
        key = str(m) + ',' + str(n)
        if key in memo:
            return memo[key]
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1

        memo[key] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)

        return memo[key]
        