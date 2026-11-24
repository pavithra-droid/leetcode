def closest_sum(nums, target):
    nums.sort()

    closest_diff = float("inf")
    closest = None

    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        diff = abs(target - total)

        if diff < closest_diff:
            diff = closest_diff
            closest = (nums[left], nums[right])

        if total == target:
            return total, closest
        elif total < target:
            left += 1
        else:
            right -= 1

    return sum(closest), closest
        


print(closest_sum([1,5,9,10,2], 8))
print(closest_sum([1,5,3,7], 8))