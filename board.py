import pygame
import numpy as np

BOARD_ROWS = 9
BOARD_COLS = 9
NUM_NUMS = 9

# UPDATE: I began trying to solve the way that the website recommended before 
# I realized it wasn't recursive backtracking. So we may want to completely redo
# this later

class Board:
    def __init__(self):
        # board has 9 rows x 9 columns of cells. Each cell has 9
        # possible numbers in it, kept track of with 3rd dimension of array
        self.board = np.zeroes((BOARD_ROWS, BOARD_COLS, NUM_NUMS))
        solved = False

    def generate_complete_grid(self):
        print("unfinished")

    def solve_easy(self):
        while (not solved):
            for row in range(1, 10):
                for i in range(1, 10):
                    # check if that number has only one place to insert
                    print("unfinished")

            for col in range(1, 10):
                for i in range(1, 10):
                    # check if that number has only one place to insert
                    print("unfinished")

            for box in range(1, 10):
                for i in range(1, 10):
                    # check if that number has only one place to insert
                    print("unfinished")

            # if the board has been solved
            if ():
                solved = not solved