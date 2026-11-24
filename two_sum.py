def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        compliment = target - num

        if compliment in seen:
            return [seen[compliment], index]

        seen[num] = index

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))

