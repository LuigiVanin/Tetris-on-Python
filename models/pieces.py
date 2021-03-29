class Piece():
    def __init__(self):
        self.x = 4
        self.y = 0

    def moveDown(self):
        self.y += 1

    def moveUp(self):
        self.y -= 1

    def moveLeft(self): # tentar evitar teletransporte 
        if self.x - 1 != -1:
            self.x -= 1

    def moveRight(self): # tentar evitar telettransporte
        self.x += 1

class PieceA(Piece):

    def __init__(self):
        super().__init__()
        self.center_pos = (1,1)
        self.type = 1
        self.format = [[1,0], [1,0], [1,0], [1,1]]

class PieceB(Piece):

    def __init__(self):
        super().__init__()
        self.type = 2
        self.format = [[1,1], [1,1]]

class PieceC(Piece):

    def __init__(self):
        super().__init__()
        self.type = 3
        self.format = [[1,1,1,1]]

class PieceD(Piece):

    def __init__(self):
        super().__init__()
        self.type = 4
        self.format = [[1,1,1], [0,1,0]]

class PieceE(Piece):

    def __init__(self):
        super().__init__()
        self.type = 5
        self.format = [[1,0], [1,1], [0, 1]]