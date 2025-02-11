class Distance:
    def __init__(self, km) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, number):
        return Distance(round(self.km * number, 2))

    def __truediv__(self, number):
        return Distance(round(self.km / number, 2))

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __len__(self):
        return self.km
