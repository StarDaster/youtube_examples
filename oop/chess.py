from abc import ABC, abstractmethod


class ChessField:
    def __init__(self):
        pass


class Figure(ABC):
    @abstractmethod
    def move(self, coord_a: str, coord_b: str):
        pass


class Queen(Figure):
    def move(self, coord_a: str, coord_b: str):
        pass
