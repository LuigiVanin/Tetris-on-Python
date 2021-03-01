
class Piece():
    def __init__(self):
        self.x = 4
        self.y = 0
        self.type = 1

    def moveDown(self):
        self.y += 1

class PieceA(Piece):

    def __init__(self):
        super().__init__()
        self.format = [[1,1,1],[0,0,1]]

class PieceB(Piece):
    def __init__(self):
        super.__init__()
  
