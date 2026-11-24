from collections import Counter

def top_k_frequent_elements(nums, k):
    freq = Counter(nums)
    result = [
        key for key, _ in 
        sorted(freq.items(), key=lambda x:x[1], reverse=True)]
    return result[:k]

print(top_k_frequent_elements([1,1,1,2,2,3], k=2))


def top_k_freq(nums, k):
    counter = Counter(nums)
    return [key for key, value in counter.most_common(k)]

print(top_k_freq([1,1,1,2,2,3], k=2))

import heapq

def top_k_heap(nums, k):
    freq = Counter(nums)

    heap = []

    for key, value in freq.items():
        heapq.heappush(heap,(value, key))

        if len(heap) > k:
            heapq.heappop(heap)
    return [j for i, j in heap]

print(top_k_heap([1, 1, 1, 2, 2, 3], k=2))