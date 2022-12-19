class Modulator(object):
    def modulo(self, other: int):
        NotImplemented

    def divisable(self, other: int):
        return not self.modulo(other)


class WorryLevel(Modulator):
    def __init__(self, value: int):
        self.value = value

    def modulo(self, other: int):
        return self.value % other


class Add(Modulator):
    def __init__(self, base: Modulator, summand: int):
        self.base = base
        self.summand = summand

    def modulo(self, other: int):
        """
        It appears that:
            (x + y) % m = ((x % m) + y) % m

        This should be distributiveness.

        """
        return (self.base.modulo(other) + self.summand) % other


class Multiply(Modulator):
    def __init__(self, base: Modulator, multiplier: int):
        self.base = base
        self.multiplier = multiplier

    def modulo(self, other: int):
        return (self.base.modulo(other) * self.multiplier) % other
