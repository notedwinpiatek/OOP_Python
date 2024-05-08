import pygame
from sys import exit

# initialization
pygame.init()
pygame.display.set_caption('Bounce King')

# variables
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/Warzone.ttf', 35)
score_font = pygame.font.Font('font/Warzone.ttf', 20)
start_time = 0
score = 0
game_active = False

# background
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
ground_rectangle = ground_surface.get_rect(topleft = (0,300))

# text
text_surface = text_font.render('BOunce King', False, 'Black' )
text_rectangle = text_surface.get_rect(center = (400,50))
game_over = text_font.render("Game Over", False, (64,64,64))
game_over_rectangle = game_over.get_rect(center = (400,180))
restart = score_font.render("Press Enter to restart", False, (64,64,64))
restart_rectangle = restart.get_rect(center = (400,220))


def display_time():
    current_time = int((pygame.time.get_ticks()/1000) - start_time)
    score_surface = score_font.render(f'SCORE: {current_time}', False, 'Black' )
    score_rectangle = score_surface.get_rect(topleft = (20,20))
    screen.blit(score_surface, score_rectangle)
    return current_time

# snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (850,300))

# player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0
player_stand = pygame.image.load('graphics/Player/player_stand.png')
player_stand_rectangle = player_stand.get_rect(center  = (400,200))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_surface = pygame.image.load('graphics/Player/jump.png').convert_alpha()
                if player_rectangle.bottom >= 300:
                    player_gravity = -25
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
                player_surface = pygame.image.load('graphics/Player/jump.png').convert_alpha()
                if player_rectangle.bottom >= 300:
                    player_gravity = -25                   
    
        if event.type == pygame.KEYDOWN and not game_active:
            if event.key == pygame.K_RETURN:
                snail_rectangle.x = 800
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
               
    if game_active:
        # background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, ground_rectangle)

        # text
        screen.blit(text_surface, (text_rectangle))

        # snail
        snail_rectangle.x -= 3
        if snail_rectangle.right <= 0:
            snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)

        # player
        screen.blit(player_surface, player_rectangle)
        player_gravity +=1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom > 300:
            player_rectangle.bottom = 300
            player_gravity = 0
            player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

        score = display_time()

        if snail_rectangle.colliderect(player_rectangle):
            game_active = False

    else:
        if score != 0:
            screen.fill('#c0e8ec')
            screen.blit(game_over,game_over_rectangle)
            screen.blit(restart,restart_rectangle)
            # game message 
            game_message = score_font.render(f"Your score is: {score}",False, (64,64,64))
            game_message_rectangle = game_message.get_rect(center = (400,350))
            screen.blit(game_message, game_message_rectangle)
        else:
            screen.fill('#c0e8ec')
            screen.blit(player_stand, player_stand_rectangle)


    pygame.display.update()
    clock.tick(60)