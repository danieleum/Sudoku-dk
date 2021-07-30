import pygame
from board import Board

WIDTH, HEIGHT = 800, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 9


def main():
    
    run = True
    board = Board()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.place(23, 3)
        draw_window(board)
                
    pygame.quit()


def draw_window(board):
    WINDOW.fill(WHITE)
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(WINDOW, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4) 
            pygame.draw.line(WINDOW, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(WINDOW, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2) 
        pygame.draw.line(WINDOW, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    
    for i in range(SIZE):
        for j in range(SIZE):
            if (board.board[i, j] != 0):
                # draw the number pic in
                pygame.draw.line(WINDOW, BLACK, (0, 0), (50, 50), 3)

    pygame.display.update()

if __name__ == "__main__":
  main()
