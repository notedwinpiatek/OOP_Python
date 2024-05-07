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
text_surface = text_font.render('BOunce King', False, 'Black' )
text_rectangle = text_surface.get_rect(center = (400,50))

score_surface = score_font.render('SCORE:', False, 'Black' )
score_rectangle = score_surface.get_rect(topleft = (20,20))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (850,300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos):
        #         print("mouse on player")
            
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "White", text_rectangle)
    # pygame.draw.line(screen,"Red", (0,0), (800,400),10)
    pygame.draw.ellipse(screen, '#ffdd00', pygame.Rect(50, 200, 100, 100))
    screen.blit(text_surface, (text_rectangle))
    screen.blit(score_surface, score_rectangle)
    snail_rectangle.x -= 3
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)
            
    # if player_rectangle.colliderect(snail_rectangle):
    #     print("Collision")

    # mouse_position = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_position):
    #     print("mouse on player")

    pygame.display.update() 
    clock.tick(60)