import pprint

stacks = {}

input_ = iter(list(open("input.txt")))
# Gather the stack description
for line in input_:
    if not line.strip():
        break

    if "[" not in line:
        continue

    for stack in range(1, (len(line) // 4) + 1):
        column = stack * 4 - 3
        item = line[column].strip()
        if not item:
            continue

        stacks.setdefault(stack, [])
        stacks[stack].insert(0, item)


def print_stacks():
    for x in sorted(stacks):
        result = str(x) + " "
        for elem in stacks[x]:
            result += elem
        print(result)


print_stacks()

# Process the movement instructions
for line in input_:
    if not line.strip():
        break
    _, count, _, from_, _, to = line.split()
    from_ = int(from_)
    to = int(to)
    count = int(count)

    print(line)
    items = stacks[from_][-count:]
    del stacks[from_][-count:]
    stacks[to].extend(items)
    print_stacks()

result = ""
for x in sorted(stacks):
    result += stacks[x][-1]

print()
print("Result: ")
print(result)
