import pygame

WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
                
    pygame.quit()


def draw_window():
    WINDOW.fill(WHITE)
    # Draws lines of sudoku board
    for i in range(0, 541, 180):
        pygame.draw.line(WINDOW, BLACK, (i + 30, 0 + 30), (i + 30, 540 + 30), 4)
        pygame.draw.line(WINDOW, BLACK, (i + 30 + 60, 0 + 30), (i + 30 + 60, 540 + 30), 2)
        pygame.draw.line(WINDOW, BLACK, (i + 30 + 120, 0 + 30), (i + 30 + 120, 540 + 30), 2)
        pygame.draw.line(WINDOW, BLACK, (0 + 30, i + 30), (540 + 30, i + 30), 4)
        pygame.draw.line(WINDOW, BLACK, (0 + 30, i + 30 + 60), (540 + 30, i + 30 + 60), 2)
        pygame.draw.line(WINDOW, BLACK, (0 + 30, i + 30 + 120), (540 + 30, i + 30 + 120), 2)
    pygame.display.update()

if __name__ == "__main__":
  main()
