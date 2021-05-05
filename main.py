from modules.models.models import Board
from modules.utils.utils import KeyBoardMove

def main():

    buttonLeft = KeyBoardMove('a')
    buttonRight = KeyBoardMove('d')
    buttonRotate = KeyBoardMove('j')
    buttonUnRotate = KeyBoardMove('k')
    buttonSpeed = KeyBoardMove('s')

    board = Board()

    board.loadPiece()

    print(board.size)

    print("while initialize")
    while True:
        if board.updateBoardCheck.timeCheck(buttonSpeed.HoldMove):
            board.pieceDrop()
  
        buttonLeft.PressedMove(board.pieceLeft)
        buttonRight.PressedMove(board.pieceRight) 
        buttonRotate.PressedMove(board.pieceRotate)
        buttonUnRotate.PressedMove(board.pieceUnRotate)

if __name__ == "__main__":
    main()    
        