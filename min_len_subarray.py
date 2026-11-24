def min_len_subarray(nums, target):
    left = 0
    current_length = 0
    min_length = float("inf")
    total = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            current_length = right- left + 1
            min_length = min(min_length, current_length)
            total -= nums[left]
            left += 1

    return 0 if min_length == float("inf") else min_length
print(min_len_subarray([2, 3, 1, 2, 4, 3], 7))