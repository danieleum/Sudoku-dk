import pygame

class Cell:

  def __init__(self, cellNum):
    self.original = False
    self.value = 0
    self.cellNum = cellNum
    
  def __init__(self, original, value, cellNum):
    self.original = original
    self.value = value
    self.cellNum = cellNum

  def setValue(self, value):
    self.value = value

  def isOriginal(self):
    return self.original

  def getValue(self):
    return self.value
      
  def getCellNum(self):
    return self.cellNum
