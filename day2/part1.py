def parse_choice(choice):
    if choice in "AX":
        return Rock()
    if choice in "BY":
        return Paper()
    if choice in "CZ":
        return Scissors()


class Rock:

    points = 1

    def __gt__(self, other):
        return isinstance(other, Scissors)

    def __eq__(self, other):
        return isinstance(other, Rock)


class Paper:

    points = 2

    def __gt__(self, other):
        return isinstance(other, Rock)

    def __eq__(self, other):
        return isinstance(other, Paper)


class Scissors:

    points = 3

    def __gt__(self, other):
        return isinstance(other, Paper)

    def __eq__(self, other):
        return isinstance(other, Scissors)


my_points = 0

for line in open("strategyguide.txt"):
    line = line.strip()
    if not line:
        break
    other, me = [parse_choice(c) for c in line.split()]
    my_points += me.points
    if me > other:
        my_points += 6  # win
    elif me == other:
        my_points += 3  # draw

print(my_points)
