import os.path

stop = StopIteration()


def peeking(iter):
    current = next(iter)
    try:
        peek = next(iter)
    except StopIteration:
        peek = stop
    yield current, peek if peek is not stop else ""
    while peek is not stop:
        current = peek
        try:
            peek = next(iter)
        except StopIteration:
            peek = stop
        yield current, peek if peek is not stop else ""


cwd = "/"
input = peeking(iter(open("input")))

file_sizes = {}
directory_sizes = {}
total_size = 0

# Phase 1: Input parsing the "shell session" and
# building a (flat) map of the file sizes.
while True:
    try:
        line, next_line = next(input)
    except StopIteration:
        break
    line = line.strip()
    assert line.startswith("$ ")
    _, cmd, *args = line.split()
    if cmd == "cd":
        cwd = os.path.normpath(os.path.join(cwd, args[0]))
    if cmd == "ls":
        while not next_line.startswith("$ "):
            try:
                line, next_line = next(input)
            except StopIteration:
                break
            size, filename = line.split()
            if size == "dir":
                continue
            filename = os.path.join(cwd, filename)
            file_sizes[filename] = int(size)
            total_size += int(size)

# Phase 2: sum up all directory sizes
for filename, size in file_sizes.items():
    path_parts = filename.split("/")
    while len(path_parts) > 1:
        path_parts.pop()
        directory = "/".join(path_parts)
        directory_sizes.setdefault(directory, 0)
        directory_sizes[directory] += size

# Phase 3: run the report
filesystem_size = 70000000
unused_target = 30000000
currently_unused = filesystem_size - directory_sizes[""]
deletion_candidate = filesystem_size
for directory, size in directory_sizes.items():
    if size + currently_unused < unused_target:
        continue
    if deletion_candidate > size:
        deletion_candidate = size

print(deletion_candidate)
