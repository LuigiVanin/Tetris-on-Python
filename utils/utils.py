import keyboard
import random
from models.pieces import (
    PieceA, PieceB, PieceC, PieceD, PieceE
    ) # provavel erro recursivo - models.pieces <-> utils.utils

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
