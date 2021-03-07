import keyboard

class KeyPressedMove(): #tornar em um método mais inteligente
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




# def representation(matrix):
#     x, y = x #<-- shape(x)
#     representation = []
#     for x in matrix:
#         for y in x:
#             if x == 0:
#                 representaion.append('*')
#             else:
#                 representation.append(pience.representation)

#     return representation

# def pieceRotation(piece):
#     pass

# def createPiece():
#     pieces = ['A', 'B', 'C', 'D', 'E']
    
#     if piece == 'A':
#         return PieceA()
