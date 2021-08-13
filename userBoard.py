import pygame

from cell import Cell

SIZE = 9

class UserBoard:
    
    # Constructor intended for when you pass in a board with only the
    # 17 original numbers filled out.
        # Fills cells array with appropriate Cell objects
    def __init__(self, board):
      self.cells = []

      for i in range(9):
        self.cells.append([])
        for j in range(9):
          cellNum = i * SIZE + j
          if (board.board.getValue(cellNum) != 0):
              self.cells[i].append(Cell(True, board.board.getValue(cellNum), cellNum))
          else:
              self.cells[i].append(Cell(cellNum))
            
              
    # Updates the appropriate Cell with the given value
    def placeNum(self, cellNum, value):
        self.cells[cellNum // SIZE][cellNum % SIZE].setValue(value)
        

    # Clears the given Cell to a value of 0 (the null value)
    def clearCell(self, cellNum):
        self.cells[cellNum // SIZE][cellNum % SIZE].setValue(0)


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
          
      
          