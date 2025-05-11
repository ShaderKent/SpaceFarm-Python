import random
import pygame
from os.path import join

class Background(pygame.sprite.Sprite):
    def __init__(self, surface, position, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(topleft = position) 

class Player:
    pass

class Plant:
    pass

class FarmplotTile:
    pass

class Farmplot:
    pass

# General Setup
pygame.init()
pygame.display.set_caption("Space Farm")
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
main_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock() #Creates the main clock object

# Imports
island_background_surf = pygame.image.load(join("img", "MainMap.png")).convert()

# Sprites
all_sprites = pygame.sprite.Group() #Group for all sprites

island_background_sprite = Background(island_background_surf, (-5500,-4500), all_sprites)



while running:
    dt = clock.tick(60) / 1000 # Delta Time

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Handles "X"ing out of the game
            running = False

    all_sprites.draw(main_display)
    pygame.display.update()


pygame.quit() 


