import random
import pygame
from os.path import join

class Player:
    pass

class Plant:
    pass

class FarmplotTile:
    pass

class Farmplot:
    pass

# general setup
pygame.init()
pygame.display.set_caption("Space Farm")
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
main_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Handles "X"ing out of the game
            running = False

pygame.quit() 


