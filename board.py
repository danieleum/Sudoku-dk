import pygame

import numpy as np

SIZE = 9

class Board:
    def __init__(self):
        # board has 9 rows x 9 columns of cells.
        self.board = np.zeros((SIZE, SIZE))
        
        # 2D array
        rows, cols = (SIZE, SIZE)
        self.secondBoard=[]
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(0)
            self.secondBoard.append(col)
    
    def place(self, cellNumber, n):
        i = cellNumber // SIZE
        j = cellNumber % SIZE
        self.board[i, j] = n
        

    def remove(self, cellNumber):
        self.board[cellNumber / SIZE, cellNumber % SIZE] = 0
    
    def getUnassignedLocation(self) -> int:
        for i in range(SIZE):
            for j in range(SIZE):
                if (self.board[i, j] == 0):
                    return i * SIZE + j
        return -1
    
    def noConflicts(self, cellNumber, n):
        # find the row that we want to check
        rowCheck = cellNumber / SIZE
        # find the col that we want to check
        colCheck = cellNumber % SIZE
        
        # check the row
        for col in range(len(SIZE)):
            if self.board[rowCheck][col] == n and colCheck != col:
                return False

        # check the column
        for row in range(len(SIZE)):
            if self.board[row][colCheck] == n and rowCheck != row:
                return False

        # check the box
        box_row = rowCheck // 3
        box_col = colCheck // 3
        for i in range(box_col * 3, box_col * 3 + 3):
            for j in range(box_row * 3, box_row * 3 + 3):
                if self.board[i][j] == n and rowCheck != i and colCheck != j:
                    return False

        return True



    def explore(self) -> bool:
        cellNumber = self.getUnassignedLocation()
        if (cellNumber == -1):
            return True
        else:
            for i in range(1, SIZE + 1):
                if (self.noConflicts(cellNumber, i)):
                    self.place(cellNumber, i)
                    if (self.explore()):
                        return True
                    self.remove(cellNumber) 
            return False