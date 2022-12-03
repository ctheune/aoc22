priorities = 0


def to_priority(ch):
    if ch.islower():
        return ord(ch) - 96
    return ord(ch) - (96 - 58)


for i, rucksack in enumerate(open("input.txt")):
    rucksack = rucksack.strip()
    if i % 3 == 0:
        # Start a new set
        common = set(rucksack)
    elif i % 3 == 1:
        # just going on
        common = common.intersection(set(rucksack))
    else:
        # finishing this set
        common = common.intersection(set(rucksack))
        assert len(common) == 1
        priorities += to_priority(list(common)[0])

print(priorities)
