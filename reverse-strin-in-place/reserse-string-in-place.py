from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers approach
        
        left, right = 0, len(s) - 1
        # middle of array is reached when left < right
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1