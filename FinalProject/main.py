import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bounce King')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('')
# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(test_surface, (200, 100))
            
    pygame.display.update()
    clock.tick(60)