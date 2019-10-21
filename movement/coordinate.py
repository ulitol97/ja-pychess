from __future__ import annotations


class Coordinate:
    """The class coordinate represents a two dimensional location in the space of the game board given X and Y"""
    def __init__(self, x: int = None, y: int = None) -> None:
        """Initiate a new Coordinate with the input data"""
        self.x: int = x
        self.y: int = y

    def __str__(self) -> str:
        """Return a human readable representation of the Coordinate"""
        return "x: {} - y: {}".format(self.x, self.y)

    def __add__(self, other: Coordinate) -> Coordinate:
        """Add two instances of Coordinate by adding up their inner coordinates"""
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Coordinate) -> Coordinate:
        """Subtract two instances of Coordinate by subtracting their inner coordinates"""
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other: Coordinate) -> bool:
        """Compare two instances of Coordinate by comparing their inner coordinates"""
        return self.x == other.x and self.y == other.y
