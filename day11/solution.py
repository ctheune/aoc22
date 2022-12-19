import typing
from functools import reduce
import time


class Monkey:

    items: typing.List[int]
    operation_code: str
    divisor: int

    next_true: int
    next_false: int

    inspections: int = 0

    def __init__(self, id_):
        self.id = id_
        self.items = []

    def operation(self, old: int):
        return eval(self.operation_code, None, dict(old=old))

    def test(self, item: int) -> bool:
        return not divmod(item, self.divisor)[1]

    def round(self):
        print(f"  Monkey {self.id}: {len(self.items)} items")
        while self.items:
            item = self.items.pop(0)
            self.inspections += 1
            # monkey inspects item, worry level increases
            item = self.operation(item)
            # monkey gets bored, worry level goes down
            item = item // 3
            # monkey passes item on
            next_monkey = self.next_true if self.test(item) else self.next_false
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
    monkey.items = [int(x.strip()) for x in item_str.split(",")]

    line = next(input).strip()
    assert line.startswith("Operation:")
    operation_code = line.split(":")[1].strip()
    operation_code = operation_code.split("=")[1]
    monkey.operation_code = operation_code

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
for round in range(20):
    print(f"Round {round}")
    for id_ in sorted(monkeys):
        monkeys[id_].round()
    print()

inspections = list(m.inspections for m in monkeys.values())
inspections.sort()
inspections = inspections[-2:]
print(reduce(lambda x, y: x * y, inspections))
