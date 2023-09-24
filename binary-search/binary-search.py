from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set two pointers low and high at the lowest(index 0) and the highest(last index) positions respectively
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, left, right):
        #condition to check for valid range and stop recursion once array is empty
        if left <= right:
            mid = (left + right) // 2
            mid_element = nums[mid]

            if target == mid_element:
                return mid  # Target found at index 'mid'

            if target < mid_element:
                return self.binary_search(nums, target, left, mid - 1)  # Search in the left half
            else:
                return self.binary_search(nums, target, mid + 1, right)  # Search in the right half

        return -1  # Target not found
    
solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]

# Test case 1: Target (4) is in the array
target1 = 9
result1 = solution.search(nums, target1)
print(result1)