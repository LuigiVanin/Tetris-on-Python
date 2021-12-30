from typing import List

class Piece():
    def __init__(self):
        self.x: int = 4
        self.y: int = 0
        self.format: List[List[int]] = []

    def moveDown(self) -> None:
        self.y += 1

    def moveUp(self) -> None:
        self.y -= 1

    def moveLeft(self) -> None:
        self.x -= 1

    def moveRight(self) -> None: 
        self.x += 1

    def startPosition(self, vec : List[int]) -> None:
        if len(vec) == 2 and (self.x == 4 and self.y == 0):
            self.x = vec[0]
            self.y = vec[1]
        else:
            raise IndexError

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __iter__(self):
        for i in self.format:
            yield i

class PieceA(Piece):

    def __init__(self):
        super().__init__()
        self.center_pos = (1,1)
        self.type = 1
        self.format = [[1,0],
                       [1,0],
                       [1,1]]

class PieceB(Piece):

    def __init__(self):
        super().__init__()
        self.center_pos = (1,1)
        self.type = 2
        self.format = [[1,1],
                       [1,1]]

class PieceC(Piece):

    def __init__(self):
        super().__init__()
        self.center_pos = (1,1)
        self.type = 3
        self.format = [[1,1,1,1]]

class PieceD(Piece):

    def __init__(self):
        super().__init__()
        self.center_pos = (1,1)
        self.type = 4
        self.format = [[1,1,1], 
                       [0,1,0]]

class PieceE(Piece):

    def __init__(self):
        super().__init__()
        self.center_pos = (1,1)
        self.type = 5
        self.format = [[1,0],
                       [1,1],
                       [0, 1]]