import numpy as np
from utils.utils import updateBoardCheck
from copy import deepcopy
from .pieces import Piece


class Board():
    def __init__(self):
        self.size = (16, 10)
        self.table = np.zeros(self.size, np.int8)
        self.blank_table = deepcopy(self.table)
        self.updateBoardCheck = updateBoardCheck()
        self.pieces = []

    # def loadPiece():
   
    def _mapPiece(self):
        self._tableClear()
        self.table[self.pieces[-1].y][self.pieces[-1].x] = self.pieces[-1].type

    def loadPiece(self):
        self.pieces.append(Piece())
        self._mapPiece()
    
    def pieceDrop(self):
        self.pieces[-1].moveDown()
        self._mapPiece()
        pass
    
    def getPieceCounter(self) -> int:
        return len(self.pieces)

    def updateBoard(self):
        print('\n' * 20)
        for i in self.table:
            print(*i, sep=" ")

    def _tableClear(self):
        self.table = deepcopy(self.blank_table)
        
        

# class Piece():
#     def __init__(self):
#         self.x = 4
#         self.y = 0
#         self.type = 1

#     def moveDown(self):
#         self.y += 1

# class PieceA(Piece):

#     def __init__(self):
#         super().__init__()
#         self.format = [[1,1,1],[0,0,1]]

#     def rotate(self):
#         pass
  

# class board():
#     def __init__(self):
#         self.table = np.zeros(tetris_coordinations)
#         self.blank_table = np.zeros(tetris_coordinations)

#     def show():
#         show_board(self.board)


# class Piece():
#     def __init__(self, piece_type):
#         self.x_position = x_init
#         self.y_position = y_init
#         self.piece_type = piece_type

    
#     pass
