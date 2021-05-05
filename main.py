from modules.models.models import Board
from modules.utils.utils import KeyPressedMove


def main():

    buttonLeft = KeyPressedMove('a')
    buttonRight = KeyPressedMove('d')

    board = Board()

    board.loadPiece()

    print(board.size)

    print("while initialize")
    while True:

        if board.updateBoardCheck.updateBoardCheck(0.5) == True:
            print("worked")
            board.pieceDrop()
  
        buttonLeft.keyPressedMove(board.pieceLeft)
        buttonRight.keyPressedMove(board.pieceRight) 

if __name__ == "__main__":
    main()    
        