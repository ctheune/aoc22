import functools


class Position(tuple):
    def __add__(self, other):
        return Position([self[0] + other[0], self[1] + other[1]])


class Tree:
    def __init__(self, forest, position, height):
        self.forest = forest
        self.position = position
        self.height = height

    def walk_neighbours(self, direction):
        candidate = self
        while True:
            try:
                candidate = self.forest[candidate.position + direction]
            except KeyError:
                break
            yield candidate

    def visible(self):
        # Assume we're visible from all directions
        visible_directions = 4
        # Check all directions and reduce our visibility if we
        # encounter a tree that is at least our size
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for neighbour in self.walk_neighbours(direction):
                if neighbour.height >= self.height:
                    visible_directions -= 1
                    break
        return int(bool(visible_directions))

    def scenic_score(self):
        directional_scores = []
        # Check all directions and reduce our visibility if we
        # encounter a tree that is at least our size
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            seen_trees = 0
            for neighbour in self.walk_neighbours(direction):
                seen_trees += 1
                if neighbour.height >= self.height:
                    break
            directional_scores.append(seen_trees)
        return functools.reduce(lambda x, y: x * y, directional_scores)


# (x, y) -> Tree
forest = {}

# Parse input
for y, line in enumerate(open("input")):
    line = line.strip()
    for x, height in enumerate(line):
        position = Position([x, y])
        forest[position] = Tree(forest, position, height)

# Gather visibility for all trees
highest_scenic_score = max(x.scenic_score() for x in forest.values())

print(highest_scenic_score)
