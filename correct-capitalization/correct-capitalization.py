def corect_capitalization(s) -> bool:
    if s.isupper():
        return True
    if s.islower():
        return True
    if s[0].isupper() and s[1:].islower():
        return True
    else: 
        return False

print(corect_capitalization('USA'))
print(corect_capitalization('Calvin'))
print(corect_capitalization('compUter'))
print(corect_capitalization('coding'))