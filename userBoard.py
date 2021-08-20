import pygame
import os

import numpy as np
from cell import Cell
from board import Board

SIZE = 9

# grabbing pics of the numbers to display
ONE_PIC = pygame.image.load(os.path.join('Numbers', 'number1.png'))
ONE = pygame.transform.scale(ONE_PIC, (40,40))
TWO_PIC = pygame.image.load(os.path.join('Numbers', 'number2.png'))
TWO = pygame.transform.scale(TWO_PIC, (40,40))
THREE_PIC = pygame.image.load(os.path.join('Numbers', 'number3.png'))
THREE = pygame.transform.scale(THREE_PIC, (40,40))
FOUR_PIC = pygame.image.load(os.path.join('Numbers', 'number4.png'))
FOUR = pygame.transform.scale(FOUR_PIC, (40,40))
FIVE_PIC = pygame.image.load(os.path.join('Numbers', 'number5.png'))
FIVE = pygame.transform.scale(FIVE_PIC, (40,40))
SIX_PIC = pygame.image.load(os.path.join('Numbers', 'number6.png'))
SIX = pygame.transform.scale(SIX_PIC, (40,40))
SEVEN_PIC = pygame.image.load(os.path.join('Numbers', 'number7.png'))
SEVEN = pygame.transform.scale(SEVEN_PIC, (40,40))
EIGHT_PIC = pygame.image.load(os.path.join('Numbers', 'number8.png'))
EIGHT = pygame.transform.scale(EIGHT_PIC, (40,40))
NINE_PIC = pygame.image.load(os.path.join('Numbers', 'number9.png'))
NINE = pygame.transform.scale(NINE_PIC, (40,40))

# dictionary of the numbers
nums = {
  1: ONE,
  2: TWO,
  3: THREE,
  4: FOUR,
  5: FIVE,
  6: SIX,
  7: SEVEN,
  8: EIGHT,
  9: NINE
}

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

    def startNum(self, WINDOW):
      #font = pygame.font.SysFont(None, 40)

      for row in range(9):
        for col in range(9):
          if self.cells[row][col] != 0:
            WINDOW.blit(nums[self.cells[row][col]], (row * 50 + 55, col * 50 + 55))


    
    # Prints out a copy of the board to the console
    def printCells(self):
        for row in range(SIZE):
            for col in range(SIZE):
                print(int(self.cells[row][col]), end=" ")

            print()
          
      
          