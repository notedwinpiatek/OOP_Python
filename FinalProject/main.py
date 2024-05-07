import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bounce King')
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/Warzone.ttf', 35)
score_font = pygame.font.Font('font/Warzone.ttf', 15)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
ground_rectangle = ground_surface.get_rect(topleft = (0,300))

text_surface = text_font.render('BOunce King', False, 'Black' )
text_rectangle = text_surface.get_rect(center = (400,50))

score_surface = score_font.render('SCORE:', False, 'Black' )
score_rectangle = score_surface.get_rect(topleft = (20,20))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (850,300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_surface = pygame.image.load('graphics/Player/jump.png').convert_alpha()
                player_gravity = -20
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:
        #         player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, ground_rectangle)
    screen.blit(text_surface, (text_rectangle))
    screen.blit(score_surface, score_rectangle)
    snail_rectangle.x -= 3
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)


    player_gravity +=1
    player_rectangle.y += player_gravity
    if player_rectangle.y >= 220:
        player_rectangle.y = 220
        player_gravity = 0
        player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

    pygame.display.update() 
    clock.tick(60)