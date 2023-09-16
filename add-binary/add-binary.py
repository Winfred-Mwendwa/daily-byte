def add_binary(str1, str2):
    added_binary = bin(int(str1, 2) + int(str2, 2)) #2 means base 2 i.e. binary
    return added_binary[2:] #remove Ob prefix added when you convert to binary using the bin function

print(add_binary('1001' , '11'))