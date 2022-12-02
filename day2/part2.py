def parse_choice(choice):
    if choice in "AX":
        return Rock()
    if choice in "BY":
        return Paper()
    if choice in "CZ":
        return Scissors()


class Choice:

    wins_against = None
    looses_against = None

    def __gt__(self, other):
        return isinstance(other, self.wins_against)

    def __eq__(self, other):
        return isinstance(other, self)

    @property
    def wins_against(self):
        return globals()[self._wins_against]

    @property
    def looses_against(self):
        return globals()[self._looses_against]


class Rock(Choice):

    points = 1
    _wins_against = "Scissors"
    _looses_against = "Paper"


class Paper(Choice):

    points = 2
    _wins_against = "Rock"
    _looses_against = "Scissors"


class Scissors(Choice):

    points = 3
    _wins_against = "Paper"
    _looses_against = "Rock"


my_points = 0

for line in open("strategyguide.txt"):
    line = line.strip()
    if not line:
        break
    other, goal = line.split()
    other = parse_choice(other)

    if goal == "X":
        # want to loose
        me = other.wins_against()
    elif goal == "Y":
        # want to draw
        me = other
        my_points += 3
    elif goal == "Z":
        # want to win
        me = other.looses_against()
        my_points += 6
    else:
        breakpoint()
    my_points += me.points

print(my_points)
