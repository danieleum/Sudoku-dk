# for testing purposes

from board import Board

from userBoard import UserBoard

def testAlgo(): 
    board = Board()
    board.board3()
    #board.filledBoard1()
    board.printBoard()

    result = board.fullSolve()
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
        valid = board.generateStartingBoard()
        while (not valid):
            valid = board.generateStartingBoard()
        board.printBoard()
        solvable = board.fullSolve()
    print("Final Solved:")
    board.printBoard()

#testGenerateTilSolvable()

# checking if the board is solvable
def testNewGenerateRandBoard():
    for i in range(100000):
        board = Board()
        if (not board.generateStartingBoard()):
            #print("It worked!")
            print("Failed")

def getUserBoard():
    board = Board()
    solvable = False
    while (not solvable):
        valid = board.generateStartingBoard()
        while (not valid):
            valid = board.generateStartingBoard()
        solvable = board.fullSolve()
    print("Final Solved:")
    board.printBoard()


def testCheckSolvable():
    board = Board()
    board.generateStartingBoard()
    board.printBoard()
    print(board.checkSolvable())
    board.printBoard()

testCheckSolvable()

def testFullSolve():
    board = Board()
    if (board.generateStartingBoard()):
        board.printBoard()
        board.fullSolve()
        board.printBoard()

#testFullSolve()
