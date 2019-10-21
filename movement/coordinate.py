class Coordinate:
    """The class coordinate represents a two dimensional location in the space of the game board given X and Y"""
    def __init__(self, x=None, y=None):
        """Initiate a new Coordinate with the input data"""
        self.x = x
        self.y = y

    def __str__(self):
        """Return a human readable representation of the Coordinate"""
        return "x: {} - y: {}".format(self.x, self.y)

    def __add__(self, other):
        """Add two instances of Coordinate by adding up their inner coordinates"""
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two instances of Coordinate by subtracting their inner coordinates"""
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """Compare two instances of Coordinate by comparing their inner coordinates"""
        return self.x == other.x and self.y == other.y
