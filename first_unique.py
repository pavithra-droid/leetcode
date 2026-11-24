from collections import Counter
def first_unique(s):
    freq = Counter(s)

    for key, val in freq.items():
        if val == 1:
            return key
    return None

print(first_unique("swiss"))
print(first_unique("aabbcc"))
print(first_unique("racecars"))
print(first_unique("a"))

assert first_unique("swiss") == "w"


