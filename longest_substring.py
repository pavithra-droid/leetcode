def length_of_longest_substring(s):
    left = 0
    current_length = 0
    max_length = current_length
    seen = {}

    for right, char in enumerate(s):
        if char in seen:
            left = max(seen[char] + 1, left)
        
        seen[char] = right
        current_length = right - left + 1
        max_length = max(current_length, max_length)

    return max_length

print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring(""))
print(length_of_longest_substring("abcdef"))