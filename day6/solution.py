stream = open("input.txt").read().strip()

buffer = []

for i, char in enumerate(stream):
    buffer.append(char)
    if len(buffer) < 4:
        continue
    if len(buffer) > 4:
        buffer.pop(0)
    if len(set(buffer)) == len(buffer):
        print(i + 1)
        break
