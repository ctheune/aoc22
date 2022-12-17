import time


class Position(tuple):
    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self, other):
        return Position([self.x + other.x, self.y + other.y])

    def __mul__(self, other: int):
        return Position([self.x * other, self.y * other])

    def __sub__(self, other: "Position"):
        return Position([self.x - other.x, self.y - other.y])

    @property
    def abs_max(self):
        return max(map(abs, self))

    @property
    def non_zero(self):
        return len(list(filter(None, self)))

    @property
    def norm(self):
        return Position(
            [
                self.x // abs(self.x) if self.x else 0,
                self.y // abs(self.y) if self.y else 0,
            ]
        )


ORIGIN = Position([0, 0])


class Rope:
    def __init__(self, length):
        self.knots = [ORIGIN for i in range(length)]
        self.symbols = [str(i) for i in range(length)]
        self.symbols[0] = "H"

    def move(self, direction):
        # Update the head
        self.knots[0] += direction
        # Update the following knots
        for i, knot in enumerate(self.knots[1:], 1):
            distance = self.knots[i - 1] - knot
            if distance.abs_max > 1:
                self.knots[i] += distance.norm
        visited.update(self.knots)
        # The last knot we processed is the tail
        visited_tail.add(knot)

    def getchar(self, position):
        try:
            i = self.knots.index(position)
            return self.symbols[i]
        except Exception:
            # breakpoint()
            if position in visited_tail:
                return "#"
            return "."


MOVEMENTS = {
    "R": Position([1, 0]),
    "L": Position([-1, 0]),
    "D": Position([0, -1]),
    "U": Position([0, 1]),
}


def display():
    min_x = min([p.x for p in visited])
    max_x = max([p.x for p in visited])
    min_y = min([p.y for p in visited])
    max_y = max([p.y for p in visited])
    # sys.stdout.write("\033c")
    for y in range(max_y, min_y - 1, -1):
        line = ""
        for x in range(min_x, max_x + 1):
            p = Position([x, y])
            line += rope.getchar(p)
        print(line)

    print()
    print(len(visited_tail))
    print()
    time.sleep(0.1)


head = Position([0, 0])
tail = Position([0, 0])

visited = set()
visited.add(ORIGIN)

visited_tail = set()
visited_tail.add(ORIGIN)

rope = Rope(10)
display()

for line in open("input"):
    direction, steps = line.split()
    steps = int(steps)
    for step in range(steps):
        rope.move(MOVEMENTS[direction])
        # Use this for debugging / watching the rope move
        # print(line)
        # display()

display()
