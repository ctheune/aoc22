reconsider = 0


def expand_range(r):
    left, right = map(int, r.split("-"))
    return set(range(left, right + 1))


for pair in open("input.txt"):
    first, second = map(expand_range, pair.strip().split(","))
    if first.issubset(second) or second.issubset(first):
        reconsider += 1


print(reconsider)
