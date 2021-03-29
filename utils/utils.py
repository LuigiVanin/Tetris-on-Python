import keyboard
import random
from models.pieces import (PieceA, PieceB) # provavel erro recursivo - models.pieces <-> utils.utils

class KeyPressedMove(): 
    def __init__(self):
        self._button_toggle = False

    def keyPressedMove(self, key: str, move) -> bool: #tornar em um método mais inteligente
        if keyboard.is_pressed(key):
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

def choosePiece() -> (PieceA, PieceB):
    type = random.choice([1,2,3,4,5]) # quantidade de peças a de definir

    if (type == 1):
        return PieceA()
    # elif (type == 2):
    #     return PieceB()

    else:
        return PieceA()

