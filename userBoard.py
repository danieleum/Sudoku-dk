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
      self.init17 = []
      for i in range(9):
        for j in range(9):
          if (board[i][j] != 0):
            self.cells[i][j] = board[i][j]
            self.init17.append(i * SIZE + j)
          
              
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

    # draws the pre-inserted 17 numbers on the board
    def startNum(self, WINDOW):
      for row in range(9):
        for col in range(9):
          if self.cells[row][col] != 0:
            WINDOW.blit(nums[self.cells[row][col]], (row * 50 + 55, col * 50 + 55))

    # insert the user input
    def insert(self, WINDOW, position):
      x, y = position[0], position[1]
      run = True

      while run:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False
          if event.type == pygame.KEYDOWN:
            # just like an ascii value...
            # 48 represents 0... 49 represents 1...
            if (0 < event.key - 48 < 10 and (((x - 1) * SIZE + (y - 1)) not in self.init17)):
              pygame.draw.rect(WINDOW, (251, 247, 245), (x * 50 + 5, y * 50 + 5, 50 - 5, 50 - 5))
              userInput = event.key - 48
              self.cells[x - 1][y - 1] = userInput
              WINDOW.blit(nums[userInput], (x * 50 + 55, y * 50 + 55))
              run = False
            if (event.key == event.key.BACKSPACE or event.key == event.key.DELETE):
              pygame.draw.rect(WINDOW, (251, 247, 245), (x * 50 + 5, y * 50 + 5, 50 - 5, 50 - 5))
              self.cells[x - 1][y - 1] = 0
              run = False
            
      # update the user board
      #WINDOW.blit(nums[self.cells[x][y]], (x * 50 + 55, y * 50 + 55))

    
    # Prints out a copy of the board to the console
    def printCells(self):
        for row in range(SIZE):
            for col in range(SIZE):
                print(int(self.cells[row][col]), end=" ")

            print()
          
      
          