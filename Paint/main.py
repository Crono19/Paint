import sys

import pygame

pygame.init()

size = (1535, 800)

color = (255, 255, 255)

screen = pygame.display.set_mode(size)

screen.fill(color)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

