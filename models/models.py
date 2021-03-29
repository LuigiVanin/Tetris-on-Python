import numpy as np
from utils.utils import UpdateBoardCheck
from copy import deepcopy
from .pieces import Piece
from utils.utils import choosePiece #provavel erro recursivo - models.pieces <-> utils.utils


class Board():
    def __init__(self):
        self.size = (16, 10)
        self.table = np.zeros(self.size, np.int8)
        self.blank_table = deepcopy(self.table)
        self.updateBoardCheck = UpdateBoardCheck()
        self.pieces = []

    def loadPiece(self):
        self.blank_table = deepcopy(self.table)
        self.pieces.append(choosePiece())
        self._mapPiece()
   
    def _mapPiece(self):
        self._tableClear()

        for i in range(len(self.pieces[-1].format)):
            for j in range (len (self.pieces[-1].format[0])):
                if self.pieces[-1].format[i][j] != 0:
                    self.table[self.pieces[-1].y + i][self.pieces[-1].x + j] = self.pieces[-1].type
    
    def pieceDrop(self):
        try: # try para evitar extrapolação de índices da matriz
            self.pieces[-1].moveDown()
            self._mapPiece()
        except IndexError: # tratamento de erro de extrapolação de índice, geralmente causado pelo fim do tabuleiro 
            self.pieces[-1].moveUp()
            self._mapPiece()
            self.loadPiece()
    
    def pieceLeft(self):
        try:
            self.pieces[-1].moveLeft() # caso x extrapole para a direita assumirá a posição [-1] que é igual
                                       # ao final do tabuleiro e não um erro, gerando "teletransporte"
            self._mapPiece()
        except IndexError:
            self.pieces[-1].moveRight()
            self._mapPiece()
        finally:
            self.updateBoard()

    def pieceRight(self):
        try:
            self.pieces[-1].moveRight()
            self._mapPiece()
        except IndexError:
            self.pieces[-1].moveLeft()
            self._mapPiece()
        finally:
            self.updateBoard()
            

    def getPieceCounter(self) -> int:
        return len(self.pieces)

    def updateBoard(self):
        print('\n' * 20)
        for i in self.table:
            print(*i, sep=" ")

    def _tableClear(self):
        self.table = deepcopy(self.blank_table)
        