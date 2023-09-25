from typing import List
class Solution:
    #using bitwise XOR operation
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)

        for i, num in enumerate(nums):
            missing ^= num
            missing ^= i
        return missing
        