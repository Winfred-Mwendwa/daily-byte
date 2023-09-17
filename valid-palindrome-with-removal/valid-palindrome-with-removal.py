def valid_palindome_with_removal(s):
    def validPalindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True
    
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return validPalindrome(s, left, right-1) or validPalindrome(s, left+1, right)
        left, right = left+1, right-1
    return True
        

print(valid_palindome_with_removal('foobof'))
print(valid_palindome_with_removal('abcba'))
print(valid_palindome_with_removal('abccab'))