import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bounce King')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Warzone.ttf', 35)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('BOunce King', False, 'Black' )
# # test_surface = pygame.Surface((100, 200))
# # test_surface.fill('Red')
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (250,50))
            
    pygame.display.update()
    clock.tick(60)