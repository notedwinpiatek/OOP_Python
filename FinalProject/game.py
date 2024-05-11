import pygame
from sys import exit
from random import randint, choice
# Player Class
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
         super.__init__()
         player_standing = pygame.image.load().convert_alpha()
         player_standing_rect = player_standing.get_rect()
         player_walking1 = pygame.image.load().convert_alpha()
         player_walking1_rect = player_walking1.get_rect()
         player_walking2 = pygame.image.load().convert_alpha()
         player_walking2_rect = player_walking2.get_rect()
         
# Game window
pygame.init()
screen = pygame.display.set_mode((800,600))

# variables
game_active = False
clock = pygame.time.Clock()


# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
        # Turning off the game
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    if game_active:
        pass
    
    pygame.display.update()
    clock.tick(60)