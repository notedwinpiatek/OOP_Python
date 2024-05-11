import pygame
from sys import exit
from random import randint, choice

# Player Class
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('Graphics/Player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('Graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk1,player_walk2]
        self.player_index = 0
        self.player_surface = self.player_walk[self.player_index]
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (400,562))
        self.gravity = 0
        
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
         
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
                if player.bottom >= 300:
                    player_gravity = -20
        player.draw(screen)
    else:
        screen.fill('#c0e8ec')
    
    
    pygame.display.update()
    clock.tick(60)