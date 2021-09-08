import pygame
import os

import numpy as np
from cell import Cell
from board import Board

SIZE = 9

# grab OG pics
ONE_OG_PIC = pygame.image.load(os.path.join('OGNumbers', 'OG1.png'))
ONE_OG = pygame.transform.scale(ONE_OG_PIC, (40,40))
TWO_OG_PIC = pygame.image.load(os.path.join('OGNumbers', 'OG2.png'))
TWO_OG = pygame.transform.scale(TWO_OG_PIC, (40,40))
THREE_OG_PIC =pygame.image.load(os.path.join('OGNumbers', 'OG3.png'))
THREE_OG = pygame.transform.scale(THREE_OG_PIC, (40,40))
FOUR_OG_PIC = pygame.image.load(os.path.join('OGNumbers', 'OG4.png'))
FOUR_OG = pygame.transform.scale(FOUR_OG_PIC, (40,40))
FIVE_OG_PIC = pygame.image.load(os.path.join('OGNumbers', 'OG5.png'))
FIVE_OG = pygame.transform.scale(FIVE_OG_PIC, (40,40))
SIX_OG_PIC = pygame.image.load(os.path.join('OGNumbers', 'OG6.png'))
SIX_OG = pygame.transform.scale(SIX_OG_PIC, (40,40))
SEVEN_OG_PIC = pygame.image.load(os.path.join('OGNumbers', 'OG7.png'))
SEVEN_OG = pygame.transform.scale(SEVEN_OG_PIC, (40,40))
EIGHT_OG_PIC = pygame.image.load(os.path.join('OGNumbers', 'OG8.png'))
EIGHT_OG = pygame.transform.scale(EIGHT_OG_PIC, (40,40))
NINE_OG_PIC = pygame.image.load(os.path.join('OGNumbers', 'OG9.png'))
NINE_OG = pygame.transform.scale(NINE_OG_PIC, (40,40))

# dictionary for OG numbers
OGNums = {
  1: ONE_OG,
  2: TWO_OG,
  3: THREE_OG,
  4: FOUR_OG,
  5: FIVE_OG,
  6: SIX_OG,
  7: SEVEN_OG,
  8: EIGHT_OG,
  9: NINE_OG
}

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
            pygame.draw.rect(WINDOW, (127, 255, 212), ((row + 1) * 50 + 3, (col + 1) * 50 + 3, 50 - 4, 50 - 4))
            WINDOW.blit(nums[self.cells[row][col]], (row * 50 + 57, col * 50 + 57))

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
              WINDOW.blit(nums[userInput], (x * 50 + 7, y * 50 + 7))
              run = False
            if ((event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE) and (((x - 1) * SIZE + (y - 1)) not in self.init17)):
              pygame.draw.rect(WINDOW, (251, 247, 245), (x * 50 + 5, y * 50 + 5, 50 - 5, 50 - 5))
              self.cells[x - 1][y - 1] = 0
              run = False
            run = False
            
      # update the user board
      #WINDOW.blit(nums[self.cells[x][y]], (x * 50 + 55, y * 50 + 55))

    
    # Prints out a copy of the board to the console
    def printCells(self):
        for row in range(SIZE):
            for col in range(SIZE):
                print(int(self.cells[row][col]), end=" ")

            print()

    
          
    def checkValidSolution(self):
        for cellNumber in range(0, 81, 1):
            n = self.cells[cellNumber // SIZE][cellNumber % SIZE]
            # find the row that we want to check
            rowCheck = cellNumber // SIZE
            # find the col that we want to check
            colCheck = cellNumber % SIZE
            
            # check the row
            for col in range(SIZE):
                if (self.cells[rowCheck][col] == n and colCheck != col) or (self.cells[rowCheck][col] == 0):
                    return False

            # check the column
            for row in range(SIZE):
                if self.cells[row][colCheck] == n and rowCheck != row or (self.cells[row][colCheck] == 0):
                    return False

            # check the box
            box_row = rowCheck // 3
            box_col = colCheck // 3
            for i in range(box_col * 3, box_col * 3 + 3):
                for j in range(box_row * 3, box_row * 3 + 3):
                    if self.cells[j][i] == n and colCheck != i and rowCheck != j:
                        return False

        return True

    def getWrongCells(self):
        wrongCells = []
        for cellNumber in range(0, 81, 1):
            n = self.cells[cellNumber // SIZE][cellNumber % SIZE]
            # find the row that we want to check
            rowCheck = cellNumber // SIZE
            # find the col that we want to check
            colCheck = cellNumber % SIZE
            
            # check the row
            for col in range(SIZE):
                if (self.cells[rowCheck][col] == n and colCheck != col) or (self.cells[rowCheck][col] == 0):
                    wrongCells.append([rowCheck, col])

            # check the column
            for row in range(SIZE):
                if self.cells[row][colCheck] == n and rowCheck != row or (self.cells[row][colCheck] == 0):
                    wrongCells.append([row, colCheck])

            # check the box
            box_row = rowCheck // 3
            box_col = colCheck // 3
            for i in range(box_col * 3, box_col * 3 + 3):
                for j in range(box_row * 3, box_row * 3 + 3):
                    if self.cells[j][i] == n and colCheck != i and rowCheck != j:
                        wrongCells.append([i, j])

        return wrongCells
      
          