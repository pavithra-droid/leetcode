def first_repeating_num(nums):
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return num
    return None

print(first_repeating_num([2, 1, 3, 1, 2]))
