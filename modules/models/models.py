from config import *
from ..utils import *
from ..view import *

class Board():
    def __init__(self):
        self.size = (16, 10)
        self.table = np.zeros(self.size, np.int8)
        self.blank_table = deepcopy(self.table)
        self.updateBoardCheck = Check()
        self.pieces = []

    def _tableClear(self):
        self.table = deepcopy(self.blank_table)
   
    def _mapPiece(self):
        self._tableClear()

        for i in range(len(self.pieces[-1].format)):
            for j in range (len (self.pieces[-1].format[0])):
                if self.pieces[-1].format[i][j] != 0:
                    self.table[self.pieces[-1].y + i][self.pieces[-1].x + j] = self.pieces[-1].type
    
    def colisionCheck(self) -> bool:
        for i in range(len(self.pieces[-1].format)):
            for j in range (len (self.pieces[-1].format[0])):
                if(self.blank_table[self.pieces[-1].y + i][self.pieces[-1].x + j] != 0):
                    if self.pieces[-1].format[i][j] != 0:
                        return True

        return False   

    def loadPiece(self):
        self.checkRow()
        self.blank_table = deepcopy(self.table)
        self.pieces.append(choosePiece())
        self._mapPiece()

    def pieceDrop(self):
        try: # try para evitar extrapolação de índices da matriz
            self.pieces[-1].moveDown()
            self._mapPiece()
            if self.colisionCheck():
                raise IndexError
        except IndexError: # tratamento de erro de extrapolação de índice, geralmente causado pelo fim do tabuleiro 
            self.pieces[-1].moveUp()
            self._mapPiece()
            self.loadPiece()
        finally:
            self.showBoard()
    
    def pieceLeft(self):
        try:
            self.pieces[-1].moveLeft() # caso x extrapole para a direita assumirá a posição [-1] que é igual
                                       # ao final do tabuleiro e não um erro, gerando "teletransporte"
            self._mapPiece()
            if self.pieces[-1].x < 0 :
                raise IndexError

            if self.colisionCheck():
                raise IndexError
        except IndexError:
            self.pieces[-1].moveRight()
            self._mapPiece()
        finally:
            self.showBoard()

    def pieceRight(self):
        try:
            self.pieces[-1].moveRight()
            self._mapPiece()

            if self.colisionCheck():
                raise IndexError
        except IndexError:
            self.pieces[-1].moveLeft()
            self._mapPiece()
        finally:
            self.showBoard()
            
    def endGameCheck(self):
        pass

    def getPieceCounter(self) -> int:
        return len(self.pieces)

    def pieceUnRotate(self):
        try:
            self.pieces[-1].format = unRotateMatrix(self.pieces[-1].format)
            self._mapPiece()
            if self.colisionCheck():
                raise IndexError
        except IndexError:
            self.pieces[-1].format = rotateMatrix(self.pieces[-1].format)
            self._mapPiece()
            
        finally:
            self.showBoard()

    def pieceRotate(self):
        try:
            self.pieces[-1].format = rotateMatrix(self.pieces[-1].format)
            self._mapPiece()
            if self.colisionCheck():
                raise IndexError

        except IndexError:
            self.pieces[-1].format = unRotateMatrix(self.pieces[-1].format)
            self._mapPiece()
            
        finally:
            self.showBoard()

    def checkRow(self):
        row = self.size[0]
        column = self.size[1]
        destroy = False
        for i in range(row):
            destroy = True
            for j in range(column):
                if self.table[i][j] == 0 :
                    destroy = False
                    break
            if destroy == True:
                self.destroyRow(i)

    def destroyRow(self, row : int):
        for i in range(row, -1, -1):
            if i != 0:
                tmp = self.table[i - 1]
                self.table[i] = tmp

    def showBoard(self):
        printBoard(self.table)