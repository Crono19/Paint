import sys

import pygame

pygame.init()

size = (1550, 800)

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

