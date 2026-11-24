import heapq

def merge_sorted_list(lists):
    heap = []
    for i, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], i, 0))

    results = []

    while heap:
        value, lst_index, element_index = heapq.heappop(heap)
        print(value, lst_index, element_index)
        results.append(value)

        next_index = element_index + 1

        if next_index < len(lists[lst_index]):
            next_value = lists[lst_index][next_index]
            heapq.heappush(heap, (next_value, lst_index, next_index))
    return results


lists = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]
print(merge_sorted_list(lists))