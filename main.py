import random
import pygame
from os.path import join

class Background(pygame.sprite.Sprite):
    def __init__(self, surface, position, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(topleft = position) 
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 600

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt

class Player(pygame.sprite.Sprite):
    def __init__(self, surface, position, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(topleft = position)

    def update(self, dt):
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
farmPlot1_start_surf = pygame.image.load(join("img", "fp1-Start.png")).convert()
playerDown = pygame.image.load(join("img", "playerDown.png")).convert_alpha()


# Sprites
all_sprites = pygame.sprite.Group() #Group for all sprites
moving_background_sprites = pygame.sprite.Group() # All sprites that move with the background image

island_background_sprite = Background(island_background_surf, (-5500,-4500), (all_sprites, moving_background_sprites))
fp1_start_sprite = Background(farmPlot1_start_surf, (0, 0), (all_sprites, moving_background_sprites))

player = Player(playerDown, (WINDOW_WIDTH/2,WINDOW_HEIGHT/2 - 32), all_sprites)


while running:
    dt = clock.tick(60) / 1000 # Delta Time

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Handles "X"ing out of the game
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    for sprite in moving_background_sprites:
        sprite.direction.x = (int(keys[pygame.K_LEFT]) or int(keys[pygame.K_a])) - (int(keys[pygame.K_RIGHT]) or int(keys[pygame.K_d]))
        sprite.direction.y = (int(keys[pygame.K_UP]) or int(keys[pygame.K_w])) - (int(keys[pygame.K_DOWN]) or int(keys[pygame.K_s]))
        

    # Update
    all_sprites.update(dt)        

    # Draw
    all_sprites.draw(main_display)

    pygame.display.update()


pygame.quit() 


