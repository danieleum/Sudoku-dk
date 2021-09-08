# for testing purposes

from board import Board

from userBoard import UserBoard

import time

TIMEOUT = 3

def testAlgo(): 
    board = Board()
    board.board3()
    #board.filledBoard1()
    board.printBoard()

    origTime = time.time()
    result = board.fullSolve(TIMEOUT, origTime)
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
        solvable = board.fullSolve(TIMEOUT, time.time())
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
        solvable = board.fullSolve(TIMEOUT, time.time())
    print("Final Solved:")
    board.printBoard()


def testCheckSolvable():
    board = Board()
    board.generateStartingBoard()
    board.printBoard()
    print(board.checkSolvable())
    board.printBoard()

#testCheckSolvable()

def testFullSolve():
    board = Board()
    if (board.generateStartingBoard()):
        board.printBoard()
        board.fullSolve(TIMEOUT, time.time())
        board.printBoard()

#testFullSolve()

def grabGameBoard():
    board = Board()
    board.generateStartingBoard()
    board.printBoard()
    print()
    board.fullSolve()
    board.printBoard()

#grabGameBoard()

def testCheckValidSolution():
    board = Board()
    board.filledBoard1()
    # Print board1
    board.printBoard()
    print()
    # Should print 'True'
    print(board.checkValidSolution())
    print()
    board.place(0, 2)
    # Should print board with 2 in cell 0
    board.printBoard()
    print()
    # Should print 'False'
    print(board.checkValidSolution())

#testCheckValidSolution()

def test14vs17():
    for i in range(1):
        ogtime = time.time()
        board = Board()
        if (board.generateStartingBoard()):
            board.printBoard()
            board.fullSolve(TIMEOUT, time.time())
            board.printBoard()
        totalTime = time.time() - ogtime
        print(totalTime)

#test14vs17()

def printTest():
    board = Board()
    board.generateStartingBoard()
    temp = board.returnBoard()

    return temp

def printTest2(board):
    for row in range(9):
        for col in range(9):
            print(int(board[row][col]), end=" ")

        print()

#temp = printTest()
#printTest2(temp)

def checkUserBoardInit():
    board = Board()
    flag = board.generateStartingBoard()
    for i in range(1000):
        
        while (not flag):
            print("failed once")
            flag = board.generateStartingBoard()

checkUserBoardInit()

    




