import sys

import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            sys.exit()  # End pygame
