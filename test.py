# for testing purposes

from board import Board

def testAlgo(): 
    board = Board()
    board.board3()
    #board.filledBoard1()
    board.printBoard()

    result = board.explore()
    print(result)
    board.printBoard()

def testGenerate():
    board = Board()
    valid = board.generateRandBoard()
    while (not valid):
      valid = board.generateRandBoard()
    
    board.printBoard()

def testGenerateTilSolvable():
    solvable = False
    while (not solvable):
        board = Board()
        valid = board.generateRandBoard()
        while (not valid):
            valid = board.generateRandBoard()
        board.printBoard()
        solvable = board.explore()
    print("Final Solved:")
    board.printBoard()
    
    


testGenerateTilSolvable()
