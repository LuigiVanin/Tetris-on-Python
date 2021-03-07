#learn how to use event listener as e press
from models.models import Board
from utils.utils import KeyPressedMove
from time import time

def main():

    buttonLeft = KeyPressedMove()
    buttonRight = KeyPressedMove()

    board = Board()

    board.loadPiece()

    print(board.size)

    print("while initialize")
    while True:

        if board.updateBoardCheck.updateBoardCheck(1) == True:
            print("worked")
            board.pieceDrop()
            board.updateBoard()
  
        buttonLeft.keyPressedMove('a', board.pieceLeft) # ajustar movimentação
        buttonRight.keyPressedMove('d', board.pieceRight)

 
        
    

if __name__ == "__main__":
    main()    
        
    # programação main