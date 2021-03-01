#learn how to use event listener as e press
from models.models import Board
from utils.utils import KeyPressedGame
from time import time



def main():

    keyboard = KeyPressedGame()

    board = Board()

    board.loadPiece()

    print(board.size)

    print("while initialize")
    while True:

        if board.updateBoardCheck.updateBoardCheck(1) == True:
            print("worked")
            board.pieceDrop()
            board.updateBoard()
  
        keyboard.keyPressedOnce('q')
        
    

if __name__ == "__main__":
    main()    
        
    # programação main