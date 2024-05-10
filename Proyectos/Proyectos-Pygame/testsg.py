import pygame
import sys

pygame.init()

WIN = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    pygame.draw.circle(WIN, (255, 0, 0), (0, 200), radius=10)

    pygame.draw.circle(WIN, (255, 0, 0), (-1, 300), radius=10)

    pygame.display.update()