def is_palindrome(strs):
    return strs == strs[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))


def palindrome(strs):
    left = 0
    right = len(strs) - 1

    while left < right:
        if strs[left] != strs[right]:
            return False
        left += 1
        right -= 1
    return True

