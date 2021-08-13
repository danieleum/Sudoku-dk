import pygame

import numpy as np
from copy import copy, deepcopy
import random

SIZE = 9

class Board:
    def __init__(self):
        # board has 9 rows x 9 columns of cells.
        self.board = np.zeros((SIZE, SIZE))        
    
    def place(self, cellNumber, n):
        i = cellNumber // SIZE
        j = cellNumber % SIZE
        self.board[i][j] = n
    
    def getValue(self, cellNumber):
        return self.board[cellNumber // SIZE][cellNumber % SIZE]
        
    def clearBoard(self):
        self.board = np.zeros((SIZE, SIZE))

    def remove(self, cellNumber):
        self.board[cellNumber // SIZE][cellNumber % SIZE] = 0
    
    def getUnassignedLocation(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if (self.board[i][j] == 0):
                    return i * SIZE + j
        return -1
    
    def noConflicts(self, cellNumber, n):
        # find the row that we want to check
        rowCheck = cellNumber // SIZE
        # find the col that we want to check
        colCheck = cellNumber % SIZE
        
        # check the row
        for col in range(SIZE):
            if self.board[rowCheck][col] == n and colCheck != col:
                return False

        # check the column
        for row in range(SIZE):
            if self.board[row][colCheck] == n and rowCheck != row:
                return False

        # check the box
        box_row = rowCheck // 3
        box_col = colCheck // 3
        for i in range(box_col * 3, box_col * 3 + 3):
            for j in range(box_row * 3, box_row * 3 + 3):
                if self.board[j][i] == n and rowCheck != i and colCheck != j:
                    return False

        return True

    # Precondition: Assumes the board so far is valid
    # For a partially filled out board, this method fills out the rest
    # of the board. 
        # If it can do that with no conflicts, it returns True.
        # If it can't do that with no conflicts, it returns False.
    def fullSolve(self):
        # gets next open space first
        cellNumber = self.getUnassignedLocation()
        if (cellNumber == -1):
            return True
        else:
            for i in range(1, SIZE + 1):
                if (self.noConflicts(cellNumber, i)):
                    self.place(cellNumber, i)
                    if (self.fullSolve()):
                        return True
                    self.remove(cellNumber) 
            return False

    # Checks to see if the board is solvable, and returns the
    # board to the state it was in before it was checked
        # Returns True if solvable
        # Returns False if not
    def checkSolvable(self):
        tempBoard = deepcopy(self.board)
        
        if (self.fullSolve()):
            self.board = tempBoard
            return True
        else: 
            self.board = tempBoard
            return False
        
    

    # Prints out a copy of the board to the console
    def printBoard(self):
        for row in range(SIZE):
            for col in range(SIZE):
                print(int(self.board[row][col]), end=" ")

            print()
    
    # Tries to generate a starting board of 17 cells that is solvable
        # If the starting 17 cell positions have conflicts and can't be filled, it returns False
        # If the starting 17 cells have no conflicts with each other, it returns True and the
        # board is set to the solvable 17 cells
    def generateStartingBoard(self):
        self.clearBoard()

        # initialize possible cell numbers
        cellNumbers = []
        for i in range(0, 81):
            cellNumbers.append(i)
        
        chosenCells = []
        # generate 17 cell numbers
            # use a set to make sure none are the same
            # while (set size is less than 17), generate rand num and add to set
        while (len(chosenCells) < 17):
            check = True
            while check:
                cell = random.randrange(0, 81)
                if cell in cellNumbers:
                    chosenCells.append(cell)
                    cellNumbers.remove(cell)
                    check = False 
    

        # place 1 random value (1-9) one at a time in those cells
            # use the noConflicts method to make sure it is a valid num, otherwise regenerate
        for i in chosenCells:
            used = []
            placed = False
            while (not placed and len(used) < 9):
                val = random.randrange(1, 10)
                if (val not in used):
                    used.append(val)
                    if (self.noConflicts(i, val)):
                        self.place(i, val)
                        placed = True
            if (self.getValue(i) == 0):
                return False
        return True

    # CURRENTLY UNTESTED
    # checks if the user's input is valid once they've fully filled out the board
        # If the current board is not valid, returns False
        # If the current board is valid, returns True
    def checkValidSolution(self):
        for cellNumber in range(0, 81, 1):
            n = self.board[cellNumber // SIZE][cellNumber % SIZE]
            # find the row that we want to check
            rowCheck = cellNumber // SIZE
            # find the col that we want to check
            colCheck = cellNumber % SIZE
            
            # check the row
            for col in range(SIZE):
                if self.board[rowCheck][col] == n and colCheck != col:
                    return False

            # check the column
            for row in range(SIZE):
                if self.board[row][colCheck] == n and rowCheck != row:
                    return False

            # check the box
            box_row = rowCheck // 3
            box_col = colCheck // 3
            for i in range(box_col * 3, box_col * 3 + 3):
                for j in range(box_row * 3, box_row * 3 + 3):
                    if self.board[j][i] == n and rowCheck != i and colCheck != j:
                        return False

        return True
    
    
    # BELOW CODE FOR TESTING PURPOSE
    # loads in a solvable sudoku board
    def board1(self):
        self.clearBoard()
        self.place(0, 3)
        self.place(2, 6)
        self.place(3, 5)
        self.place(5, 8)
        self.place(6, 4)
        self.place(9, 5)
        self.place(10, 2)
        self.place(19, 8)
        self.place(20, 7)
        self.place(25, 3)
        self.place(26, 1)
        self.place(29, 3)
        self.place(31, 1)
        self.place(34, 8)
        self.place(36, 9)
        self.place(39, 8)
        self.place(40, 6)
        self.place(41, 3)
        self.place(44, 5)
        self.place(46, 5)
        self.place(49, 9)
        self.place(51, 6)
        self.place(54, 1)
        self.place(55, 3)
        self.place(60, 2)
        self.place(61, 5)
        self.place(70, 7)
        self.place(71, 4)
        self.place(74, 5)
        self.place(75, 2)
        self.place(77, 6)
        self.place(78, 3)

    def board3(self):
        self.clearBoard()
        vals = [8, 5, 7, 6, 4, 3, 8, 1, 8, 6, 9, 2, 3, 5, 3, 6, 3, 4, 9, 7, 8, 3, 9, 2, 1, 5, 7, 4, 6, 1]
        cells = [0, 4, 5, 9, 13, 15, 16, 17, 21, 22, 24, 29, 34, 36, 37, 41, 48, 50, 52, 54, 55, 58, 62, 64, 67, 68, 71, 72, 75, 79]
        for i in range(0, len(vals)):
            self.place(cells[i], vals[i])

    def filledBoard1(self):
        self.clearBoard()
        arr = [3, 1, 6, 5, 7, 8, 4, 9, 2, 5, 2, 9, 1, 3, 4, 7, 6, 8, 4, 8, 7, 6, 2, 9, 5, 3, 1, 2, 6, 3, 4, 1, 5, 9, 8, 7, 9, 7, 4, 8, 6, 3, 1, 2, 5, 8, 5, 1, 7, 9, 2, 6, 4, 3, 1, 3, 8, 9, 4, 7, 2, 5, 6, 6, 9, 2, 3, 5, 1, 8, 7, 4, 7, 4, 5, 2, 8, 6, 3, 1, 9]
        
        for i in range(0, 81):
            self.place(i, arr[i])


            