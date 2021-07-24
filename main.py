import pygame

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

WHITE = (255, 255, 255)

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
    pygame.display.update()

if __name__ == "__main__":
  main()
