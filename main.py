import pygame
import os
import time
from board import Board
from userBoard import UserBoard

WIDTH, HEIGHT = 800, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

SOLUTION_BUTTON_PIC = pygame.image.load(os.path.join('Buttons', 'CheckSolutionButton.png'))
SOLUTION_BUTTON = pygame.transform.scale(SOLUTION_BUTTON_PIC, (85, 85))

CORRECT_SOLUTION_PIC = pygame.image.load(os.path.join('Messages', 'correct.png'))
CORRECT_SOLUTION = pygame.transform.scale(CORRECT_SOLUTION_PIC, (CORRECT_SOLUTION_PIC.get_width() // 2, CORRECT_SOLUTION_PIC.get_height() // 2))

INCORRECT_SOLUTION_PIC = pygame.image.load(os.path.join('Messages', 'incorrect.png'))
INCORRECT_SOLUTION = pygame.transform.scale(INCORRECT_SOLUTION_PIC, (INCORRECT_SOLUTION_PIC.get_width() // 2, INCORRECT_SOLUTION_PIC.get_height() // 2))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 9


def main():
    
    run = True
    board = Board()
    board.generateStartingBoard()
    temp = board.returnBoard()
    user = UserBoard(temp)
    WINDOW.fill(WHITE)
    draw_window(board, user)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # button 1 is the left click
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()

                # x and y coordinates // 50 return box position w/math
                if (50 <= position[0] <= 500 and 50 <= position[1] <= 500):
                    user.insert(WINDOW, (position[0] // 50, position[1] // 50))
                
                if (600 <= position[0] <= 685 and 550 <= position[1] <= 635):
                    if (user.checkValidSolution()):
                        WINDOW.blit(CORRECT_SOLUTION, (200, 550))
                            
                    else:
                        WINDOW.blit(INCORRECT_SOLUTION, (200, 550))
                        
                    pygame.display.update()
                            

        
        pygame.display.update()
                
    pygame.quit()


def draw_window(board, user):
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(WINDOW, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4) 
            pygame.draw.line(WINDOW, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(WINDOW, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2) 
        pygame.draw.line(WINDOW, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    
    for i in range(81):
        user.startNum(WINDOW)

    WINDOW.blit(SOLUTION_BUTTON, (600, 550))
    pygame.display.update()

def draw_instruction():
    font = pygame.font.Sysfont("comicsans", 40)    

if __name__ == "__main__":
  main()
