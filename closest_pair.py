def closest_pair(nums):
    nums.sort()

    closest_diff = float("inf")
    result = None
    
    for i in range(len(nums)-1):
        diff = abs(nums[i+1] - nums[i])
        if diff < closest_diff:
            closest_diff = diff
            result = (nums[i], nums[i+1])
    return closest_diff, result

print(closest_pair([10,3,8,20,15]))
        