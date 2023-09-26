class Solution:
    def firstUniqChar(self, s: str) -> int:
        #initialize empty dictionary where the key is a character in s and the value is the count of the occurence of the character in s
        char_count = {}

        for char in s:
            #increment the count by one if the character is already in the dict
            if char in char_count:
                char_count[char] += 1
            else:
            #initialize the count to one otherwise
                char_count[char] = 1
        
        for i, char in enumerate(s):
            #return the index of the character whose count is only 1, since its unique
            if char_count[char] == 1:
                return i
        #return -1 if no unique character is found       
        return -1