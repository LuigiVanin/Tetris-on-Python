from config import *
from modules.models.pieces import * 
# from ..models import *

class KeyPressedMove(): 
    def __init__(self, key : str):
        self._button_toggle = False
        self.key = key

    def keyPressedMove(self, move) -> bool: #tornar em um método mais inteligente
        if keyboard.is_pressed(self.key):
            if self._button_toggle == False:
                move() # Lançamento da função de movimento passada no parâmetro
                self._button_toggle = True
        else:
            self._button_toggle = False 

class UpdateBoardCheck():
    def __init__(self):
        self._time = 0

    def updateBoardCheck(self, mult: float) -> bool:
        self._time += 1
        if self._time == 200000*mult:
            self._time = 0
            return True
        else:
            return False

def choosePiece() -> (PieceA, PieceB, PieceC, PieceD, PieceE):
    type = random.choice([1,2,3,4,5]) # quantidade de peças a de definir
    print(type)
    if (type == 1):
        return PieceA()
    
    elif (type == 2):
        return PieceB()

    elif (type == 3):
        return PieceC()

    elif (type == 4):
        return PieceD()

    else:
        return PieceE()

def printFormat(format : Optional[Piece], endrow : str = "\n", end : str = "\n"):
    if type(format) != list:
        format = list(format)
    for i in range(len(format)):
        for j in range(len(format[0])):
            print(format[i][j], end=", ")
        print(end=endrow)
    print(end=end)

def matrixSize(matrix):
    return (len(matrix), len(matrix[0]))

def unRotateMatrix(matrix : List[List[int]]):
    final = []
    tmp = []
    row, column = matrixSize(matrix)
    for j in range(column - 1, -1, -1):
        for i in range(row):
            tmp.append(matrix[i][j])  
        final.append(tmp)
        tmp = []

    return final

def rotateMatrix(matrix : List[List[int]]):
    final = []
    tmp = []
    row, column = matrixSize(matrix)
    for j in range(column):
        for i in range(row - 1, -1, -1):
            tmp.append(matrix[i][j])  
        final.append(tmp)
        tmp = []
    return final