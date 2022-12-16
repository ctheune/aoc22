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

    def __init__(self):
        self.pipeline = []

    def run(self):
        current_op = None
        while self.pipeline:
            current_op = self.pipeline.pop(0)
            for tick in current_op.run(self):
                self.clock += 1
                yield self.clock, self.x, current_op


cpu = CPU()

for line in open("input"):
    op, *args = line.strip().split()
    op = optable[op](*args)
    cpu.pipeline.append(op)

frequency_total = 0

for tick, x, op in cpu.run():
    print(f"{tick}\t{x}\t{op}")
    if tick in [20, 60, 100, 140, 180, 220]:
        frequency_total += tick * x

print(frequency_total)
