import pygame
from sys import exit
from random import randint


def obsticle_movement(obsticle_list):
    if obsticle_list:
        for obsticle_rect in obsticle_list:
            obsticle_rect.x -= 5

            if obsticle_rect.bottom ==300:
                screen.blit(snail_surface,obsticle_rect)
            else:
                screen.blit(fly_surface,obsticle_rect)


        obsticle_list = [obsticle for obsticle in obsticle_list if obsticle.x > -100]

        return obsticle_list
    else: 
        return []
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

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

# obsticles
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()



obsticle_rect_list = []

# player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0
player_stand = pygame.image.load('graphics/Player/player_stand.png')
player_stand_rectangle = player_stand.get_rect(center  = (400,200))


# timer
obsticle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obsticle_timer, 1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            # Space Jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_surface = pygame.image.load('graphics/Player/jump.png').convert_alpha()
                    if player_rectangle.bottom >= 300:
                        player_gravity = -20
            #  Mouse Jump 
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_surface = pygame.image.load('graphics/Player/jump.png').convert_alpha()
                if player_rectangle.bottom >= 300:
                    player_gravity = -20       


            # Timer
            if event.type == obsticle_timer:
                if randint(0,2):
                    obsticle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100),300)))
                else:
                    obsticle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1100),210)))

        else:   
            # game restart
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # snail_rectangle.x = 800
                    game_active = True
                    start_time = int(pygame.time.get_ticks()/1000)
        
        
    if game_active:
        # background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, ground_rectangle)

        # text
        screen.blit(text_surface, (text_rectangle))

        # snail
        # snail_rectangle.x -= 3
        # if snail_rectangle.right <= 0:
        #     snail_rectangle.left = 800
        # screen.blit(snail_surface, snail_rectangle)
        score = display_time()

        # player
        screen.blit(player_surface, player_rectangle)
        player_gravity +=1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom > 300:
            player_rectangle.bottom = 300
            player_gravity = 0
            player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        
        # Obsticle Movement
        obsticle_rect_list = obsticle_movement(obsticle_rect_list)
        # Collisions
        game_active = collisions(player_rectangle, obsticle_rect_list)



    else:
        if score != 0:
            screen.fill('#c0e8ec')
            screen.blit(game_over,game_over_rectangle)
            screen.blit(restart,restart_rectangle)
            obsticle_rect_list.clear()
            player_rectangle.midbottom = (80,300)
            player_gravity = 0
            # game message 
            game_message = score_font.render(f"Your score is: {score}",False, (64,64,64))
            game_message_rectangle = game_message.get_rect(center = (400,350))
            screen.blit(game_message, game_message_rectangle)
        else:
            screen.fill('#c0e8ec')
            screen.blit(player_stand, player_stand_rectangle)


    pygame.display.update()
    clock.tick(60)