import pygame
import os

import numpy as np
from cell import Cell
from board import Board

SIZE = 9

ONE = pygame.image.load(os.path.join('Numbers', 'number1.png'))
ONE_SIZE = pygame.transform.scale(ONE, (60,60))

class UserBoard:
    
    # Constructor intended for when you pass in a board with only the
    # 17 original numbers filled out.
        # Fills cells array with appropriate Cell objects
    def __init__(self, board):
      self.cells = np.zeros((SIZE, SIZE)) 

      for i in range(9):
        for j in range(9):
          if (board[i][j] != 0):
            self.cells[i][j] = board[i][j]
          
              
    # Updates the appropriate Cell with the given value
    def placeNum(self, cellNum, value):
        self.cells[cellNum // SIZE][cellNum % SIZE] = value
        print()
        

    # Clears the given Cell to a value of 0 (the null value)
    def clearCell(self, cellNum):
        self.cells[cellNum // SIZE][cellNum % SIZE] = 0
        print()


    # Resets the board to be all 0's except the original 17 values
    def resetBoard(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if (not self.cells[i][j].isOriginal()):
                    self.cells[i][j].setValue(0)
                

    # convert to 2d array to check if the solution is valid
    def convertFinalArray(self):
      result = []
      
      for row in range(9):
        temp = []
        for col in range(9):
          temp.append(self.cells[row][col].getValue())

        result.append(temp)

      return result

    def drawNum(self, cellNum, WINDOW):
      #font = pygame.font.SysFont(None, 40)

      row = cellNum // SIZE
      col = cellNum % SIZE

      WINDOW.blit(ONE_SIZE, (0,0))

      
        


    
    # Prints out a copy of the board to the console
    def printCells(self):
        for row in range(SIZE):
            for col in range(SIZE):
                print(int(self.cells[row][col]), end=" ")

            print()
          
      
          