import pygame
import os
import time
from board import Board
from userBoard import UserBoard

WIDTH, HEIGHT = 800, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

INSTRUCTIONS_PIC = pygame.image.load(os.path.join('Messages', 'instruction.png'))
INSTRUCTIONS = pygame.transform.scale(INSTRUCTIONS_PIC, (int(INSTRUCTIONS_PIC.get_width() * 1.5), int(INSTRUCTIONS_PIC.get_height() * 1.5)))

SOLUTION_BUTTON_PIC = pygame.image.load(os.path.join('Buttons', 'CheckSolutionButton.png'))
SOLUTION_BUTTON = pygame.transform.scale(SOLUTION_BUTTON_PIC, (85, 85))

SOLVE_BUTTON_PIC = pygame.image.load(os.path.join('Buttons', 'recursivePic.png'))
SOLVE_BUTTON = pygame.transform.scale(SOLVE_BUTTON_PIC, (SOLVE_BUTTON_PIC.get_width() // 2, SOLVE_BUTTON_PIC.get_height() // 2))

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
    flag = board.generateStartingBoard()
    while (not flag):
        flag = board.generateStartingBoard()
    #board.filledBoard1()
    temp = board.returnBoard()
    user = UserBoard(temp)
    WINDOW.fill(WHITE)
    draw_window(board, user)
    display_cor_sol = False
    display_inc_sol = False
    start_time = time.time()
    conflicting_cells = []
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
                        display_cor_sol = True
                        start_time = time.time()
                    else:
                        conflicting_cells = user.getWrongCells()
                        display_inc_sol = True
                        start_time = time.time()
                        
                    pygame.display.update()
                
                if (525 <= position[0] <= 525 + SOLVE_BUTTON.get_width() and 450 <= position[1] <= 450 + SOLVE_BUTTON.get_height()):
                    print("Solve button was clicked")
                            
        if (display_cor_sol and time.time() - start_time < 3):
            WINDOW.blit(CORRECT_SOLUTION, (200, 550))
        elif (display_cor_sol and time.time() - start_time >= 3): 
            display_cor_sol = False
            pygame.draw.rect(WINDOW, (255, 255, 255), (200, 550, CORRECT_SOLUTION_PIC.get_width() // 2, CORRECT_SOLUTION_PIC.get_height() // 2))
        
        if (display_inc_sol and time.time() - start_time < 3):
            WINDOW.blit(INCORRECT_SOLUTION, (200, 550))
            drawAllWrongAns(WINDOW, conflicting_cells, (255, 0, 0))
        elif (display_inc_sol and time.time() - start_time >= 3): 
            display_inc_sol = False
            drawAllWrongAns(WINDOW, conflicting_cells, (0, 0, 0))
            pygame.draw.rect(WINDOW, (255, 255, 255), (200, 550, INCORRECT_SOLUTION_PIC.get_width() // 2, INCORRECT_SOLUTION_PIC.get_height() // 2))
        
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

    WINDOW.blit(SOLVE_BUTTON, (525, 450))
    WINDOW.blit(SOLUTION_BUTTON, (600, 550))
    WINDOW.blit(INSTRUCTIONS, (525, 85))
    pygame.display.update()

def drawAllWrongAns(WINDOW, conflicting_cells, color):
    for i in range(len(conflicting_cells)):
        drawWrongAns(WINDOW, conflicting_cells[i][0], conflicting_cells[i][1], color)

def drawWrongAns(WINDOW, row, col, color):
    pygame.draw.line(WINDOW, color, ((row + 1) * 50, (col + 1) * 50), ((row + 1) * 50, (col + 1) * 50 + 50), 2)
    pygame.draw.line(WINDOW, color, ((row + 1) * 50 + 50, (col + 1) * 50), ((row + 1) * 50 + 50, (col + 1) * 50 + 50), 2)

    pygame.draw.line(WINDOW, color, ((row + 1) * 50, (col + 1) * 50), ((row + 1) * 50 + 50, (col + 1) * 50), 2)
    pygame.draw.line(WINDOW, color, ((row + 1) * 50, (col + 1) * 50 + 50), ((row + 1) * 50 + 50, (col + 1) * 50 + 50), 2)

def draw_instruction():
    font = pygame.font.Sysfont("comicsans", 40)    

if __name__ == "__main__":
  main()
