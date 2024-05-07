import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bounce King')
clock = pygame.time.Clock()
# test_font = pygame.font.Font()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
# # test_surface = pygame.Surface((100, 200))
# # test_surface.fill('Red')
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 400))
            
    pygame.display.update()
    clock.tick(60)