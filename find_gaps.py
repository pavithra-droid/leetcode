def find_gaps(ranges):
    result = []

    for i in range(10):
        interval = [i, i + 1]
        print(interval)

        covered = False
        for start, end in ranges:
            print(start, end)
            if start <= i and i + 1 <= end:
                covered = True
                break

        if not covered:
            result.append(interval)

    return result


ranges = [[1, 2], [4, 5], [6, 8], [9, 10]]
print(find_gaps(ranges))