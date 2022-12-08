stream = open("input.txt").read().strip()

buffer = []
buffer_size = 14

for i, char in enumerate(stream):
    buffer.append(char)
    if len(buffer) < buffer_size:
        continue
    if len(buffer) > buffer_size:
        buffer.pop(0)
    if len(set(buffer)) == len(buffer):
        print(i + 1)
        break
