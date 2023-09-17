def longest_common_prefix(strs: list[str]) -> str:
    # Case of empty strs
    if not strs:
        return ""

    # Find shortest string for reference based on length - longest common prefix cannot be longer than the shortest string
    shortest_str = min(strs, key=len)

    # Iterate through the characters of the shortest string
    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char: 
                #break and return shortest string excluding char at current index
                return shortest_str[:i]

    # If the loop completes without returning, the entire shortest string is the common prefix
    return shortest_str


print(longest_common_prefix(['flour', 'flew', 'floor']))
print(longest_common_prefix(["colorado", "color", "cold"]))
print(longest_common_prefix(["a", "b", "c"]))
print(longest_common_prefix(["spot", "spotty", "spotted"]))