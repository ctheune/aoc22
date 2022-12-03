priorities = 0
for rucksack in open("input.txt"):
    rucksack = rucksack.strip()
    middle = len(rucksack) // 2
    comp1, comp2 = set(rucksack[:middle]), set(rucksack[middle:])
    common = comp1.intersection(comp2)
    assert len(common) == 1
    common = list(common)[0]
    if common.islower():
        priorities += ord(common) - 96
    else:
        priorities += ord(common) - (96 - 58)

print(priorities)
