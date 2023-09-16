def valid_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalpha())
    return cleaned_s ==  cleaned_s[::-1]

print(valid_palindrome("A man, a plan, a canal, Panama"))
print(valid_palindrome("Algorithm"))
print(valid_palindrome("level"))