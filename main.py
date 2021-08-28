import pygame
import os
from board import Board
from userBoard import UserBoard

WIDTH, HEIGHT = 800, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

SOLUTION_BUTTON_PIC = pygame.image.load(os.path.join('Buttons', 'CheckSolutionButton.png'))
SOLUTION_BUTTON = pygame.transform.scale(SOLUTION_BUTTON_PIC, (40,40))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 9


def main():
    
    run = True
    board = Board()
    board.generateStartingBoard()
    temp = board.returnBoard()
    user = UserBoard(temp)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # button 1 is the left click
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()

                # x and y coordinates // 50 return box position w/math
                user.insert(WINDOW, (position[0] // 50, position[1] // 50))

        draw_window(board, user)
        pygame.display.update()
                
    pygame.quit()


def draw_window(board, user):
    WINDOW.fill(WHITE)
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(WINDOW, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4) 
            pygame.draw.line(WINDOW, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(WINDOW, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2) 
        pygame.draw.line(WINDOW, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    
    for i in range(81):
        user.startNum(WINDOW)
    pygame.display.update()

if __name__ == "__main__":
  main()
