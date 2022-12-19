import typing
from functools import reduce, cache


class Modulator(object):
    def modulo(self, other: int):
        NotImplemented

    def divisible(self, other: int):
        return not self.modulo(other)


class WorryLevel(Modulator):
    def __init__(self, value: int):
        self.value = value

    @cache
    def modulo(self, other: int):
        return self.value % other


class Add(Modulator):
    def __init__(self, base: Modulator, summand: int):
        self.base = base
        self.summand = summand

    @cache
    def modulo(self, other: int):
        """
        It appears that:
            (x + y) % m = ((x % m) + y) % m

        This should be distributiveness.

        """
        return (self.base.modulo(other) + self.summand) % other


class Multiply(Modulator):
    def __init__(self, base: Modulator, multiplier: int | str):
        self.base = base
        self.multiplier = multiplier

    @cache
    def modulo(self, other: int):
        multiplier = self.multiplier
        if multiplier == "old":
            multiplier = self.base.modulo(other)
        return (self.base.modulo(other) * multiplier) % other


OPERATIONS = {"*": Multiply, "+": Add}


class Monkey:

    items: typing.List[Modulator]
    operation: object  # factory for Modulator
    arg: int | str  # arg for the factory

    divisor: int

    next_true: int
    next_false: int

    inspections: int = 0

    def __init__(self, id_):
        self.id = id_
        self.items = []

    def round(self):
        print(f"  Monkey {self.id}: {len(self.items)} items")
        while self.items:
            item = self.items.pop(0)
            self.inspections += 1
            # monkey inspects item, worry level increases
            item = self.operation(item, self.arg)
            # monkey passes item on
            next_monkey = (
                self.next_true if item.divisible(self.divisor) else self.next_false
            )
            monkeys[next_monkey].items.append(item)


monkeys: typing.Dict[int, Monkey] = {}


input = iter(open("input"))
for line in input:
    assert line.startswith("Monkey")
    line = line.strip().strip(":")
    id_ = int(line.split()[-1])
    monkey = monkeys[id_] = Monkey(id_)

    line = next(input).strip()
    assert line.startswith("Starting items:")
    item_str = line.strip().split(":")[1]
    monkey.items = [WorryLevel(int(x.strip())) for x in item_str.split(",")]

    line = next(input).strip()
    assert line.startswith("Operation:")
    operation_code = line.split(":")[1].strip()
    operation_code = operation_code.split("=")[1].strip()
    _, operator, arg = operation_code.split()
    monkey.operation = OPERATIONS[operator]
    if arg == "old":
        monkey.arg = arg
    else:
        monkey.arg = int(arg)

    line = next(input).strip()
    assert line.startswith("Test: divisible by")
    monkey.divisor = int(line.split()[-1])

    line = next(input).strip()
    assert line.startswith("If true: throw to monkey")
    monkey.next_true = int(line.split()[-1])

    line = next(input).strip()
    assert line.startswith("If false: throw to monkey")
    monkey.next_false = int(line.split()[-1])

    try:
        line = next(input).strip()
        assert not line
    except StopIteration:
        break

# Start simulation
for round in range(10000):
    print(f"Round {round}")
    for id_ in sorted(monkeys):
        monkeys[id_].round()
    print()

inspections = list(m.inspections for m in monkeys.values())
inspections.sort()
inspections = inspections[-2:]
print(reduce(lambda x, y: x * y, inspections))
