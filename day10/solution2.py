class Operation:
    def run(self, cpu):
        """A generator that yields on every tick."""
        pass


class Noop(Operation):
    def run(self, cpu):
        yield

    def __repr__(self):
        return "noop"


class AddX(Operation):
    def __init__(self, value):
        self.value = int(value)

    def run(self, cpu):
        yield
        yield
        cpu.x += self.value

    def __repr__(self):
        return f"addx {self.value}"


optable = {"noop": Noop, "addx": AddX}


class CPU:
    pipeline: list = None

    # Counting the ticks
    clock: int = 0

    # The register
    x: int = 1

    def __init__(self, crt):
        self.pipeline = []
        self.crt = crt

    def run(self):
        current_op = None
        while self.pipeline:
            current_op = self.pipeline.pop(0)
            for tick in current_op.run(self):
                self.clock += 1
                yield self.clock, self.x, current_op
                self.crt.update(self.x)


class CRT:

    position: int = 0
    row: int = 0

    def __init__(self):
        self.buffer = 40 * ["."]

    def update(self, x):
        if self.position in set([x - 1, x, x + 1]):
            char = "#"
        else:
            char = "."
        self.buffer[self.position] = char
        self.position += 1
        if self.position >= 40:
            self.flush()

    def flush(self):
        print(" ".join(self.buffer))
        self.buffer = 40 * ["."]
        self.position = 0


cpu = CPU(crt=CRT())


for line in open("input"):
    op, *args = line.strip().split()
    op = optable[op](*args)
    cpu.pipeline.append(op)

for tick, x, op in cpu.run():
    pass
