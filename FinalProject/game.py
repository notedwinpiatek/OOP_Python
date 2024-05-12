import pygame
from sys import exit
from random import randint, choice

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_standing = pygame.image.load('Graphics/Player/player_stand.png').convert_alpha()
        self.player_jump = pygame.image.load('Graphics/Player/jump.png').convert_alpha()
        self.image = self.player_standing
        self.rect = self.image.get_rect(midbottom = (400,562))
        self.player_gravity = 0
    
         
# Game window
pygame.init()
screen = pygame.display.set_mode((800,600))
how_to_play = pygame.image.load('Graphics/how_to_play.png').convert_alpha()
htp_rect = how_to_play.get_rect(topleft = (0,0))

# variables
game_active = False
clock = pygame.time.Clock()

# Background
ground_surf = pygame.image.load('Graphics/ground.png').convert_alpha()
ground_rect = ground_surf.get_rect(topleft = (0,0))

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())


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
        # Starting the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_active = True
        # Game window
        screen.fill('#b0ceff')
        screen.blit(ground_surf, ground_rect)
        screen.blit(how_to_play, htp_rect)
        
        
    if game_active:
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
    # Space Jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.bottom >= 562:
                    player_gravity = -20
        player.draw(screen)
        player.update()
    else:
        screen.fill('#c0e8ec')
    
    
    pygame.display.update()
    clock.tick(60)