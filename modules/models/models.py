# pylint: disable=unused-wildcard-import
from config import *
from ..utils import *
from ..view import *

class Board():
    def __init__(self):
        self.size: Tuple[int] = (16, 10)
        self.table = np.zeros(self.size, np.int8)
        self.blank_table = deepcopy(self.table)
        self.updateBoardCheck = Check()
        self.pieces: List = []


    def _tableClear(self) -> None:
        self.table = deepcopy(self.blank_table)
   

    def _mapPiece(self) -> None:
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


    def gameOverCheck(self) -> None:
        if self.colisionCheck():
            exit()
        else:
            pass


    def loadPiece(self) -> None:
        self.checkRow()
        self.blank_table = deepcopy(self.table)
        self.pieces.append(choosePiece())
        self.gameOverCheck()
        self._mapPiece()

    def pieceDrop(self) -> None:
        try: 
            self.pieces[-1].moveDown()
            self._mapPiece()
            if self.colisionCheck():
                raise IndexError
        except IndexError:  
            self.pieces[-1].moveUp()
            self._mapPiece()
            self.loadPiece()
        finally:
            self.showBoard()
    
    def pieceLeft(self) -> None:
        try:
            self.pieces[-1].moveLeft() 
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


    def pieceRight(self) -> None:
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


    def getPieceCounter(self) -> int:
        return len(self.pieces)


    def pieceUnRotate(self) -> None:
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


    def pieceRotate(self) -> None:
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


    def checkRow(self) -> None:
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


    def destroyRow(self, row : int) -> None:
        for i in range(row, -1, -1):
            if i != 0:
                tmp = self.table[i - 1]
                self.table[i] = tmp


    def showBoard(self) -> None:
        printBoard(self.table)
