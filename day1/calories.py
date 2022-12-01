calories_and_elf = []
current_calories = 0
current_elf = 1

for line in open("elves.txt"):
    line = line.strip()
    if not line:
        # new elve
        calories_and_elf.append((current_calories, current_elf))
        current_calories = 0
        current_elf += 1
        continue
    current_calories += int(line)

calories_and_elf.sort(reverse=True)


print(sum(x[0] for x in calories_and_elf[:3]))
