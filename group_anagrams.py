from collections import defaultdict
def group_anagrams(strs):
    counter = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        counter[key].append(word)

    return list(counter.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
