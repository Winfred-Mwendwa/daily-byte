class Solution:
    def longestConsecutive(self,nums):
        num_set = set(nums) #[100,4,200,1,3,2]
        longest_sequence = 0  #space: O(n) time: O(n)

        # Iterate over "nums" and check if it's previous number exist or not.
        #If it exist , then sequence can't start from that number , so we will move to next number
        #If it doesn't exist , it means sequence can start from that number
        for num in num_set:
            if num - 1 not in num_set:  
                current_num = num
                current_sequence = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence