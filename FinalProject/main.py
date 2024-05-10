import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk1,player_walk2]
        self.player_index = 0
        self.player_surface = self.player_walk[self.player_index]
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index+= 0.1
            if self.player_index >= len(self.player_walk):self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obsticle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
    
        if type == 'fly':
            fly_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300


        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

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
                obsticle_group.empty()
                return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obsticle_group,False):
        obsticle_group.empty()
        return False
    else: return True

def player_animation():
    global player_surface,player_index
    if player_rectangle.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

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

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obsticle_group = pygame.sprite.Group()


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
snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]



obsticle_rect_list = []

# player
player_walk1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0
player_surface = player_walk[player_index]
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0
player_stand = pygame.image.load('graphics/Player/player_stand.png')
player_stand_rectangle = player_stand.get_rect(center  = (400,200))


# timer
obsticle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obsticle_timer, 1500)

snail_animation_timer = pygame.USEREVENT +2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT +3
pygame.time.set_timer(fly_animation_timer,200)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            # Space Jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rectangle.bottom >= 300:
                        player_gravity = -20
            #  Mouse Jump 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.bottom >= 300:
                    player_gravity = -20       

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface= snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface= fly_frames[fly_frame_index]

            # Timer
            if event.type == obsticle_timer:
                obsticle_group.add(Obsticle(choice(['fly','snail','snail','snail'])))
                # if randint(0,2):
                #     obsticle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100),300)))
                # else:
                #     obsticle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1100),210)))

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
        score = display_time()

        # player
        # player_gravity +=1
        # player_rectangle.y += player_gravity
        # if player_rectangle.bottom > 300:
        #     player_rectangle.bottom = 300
        #     player_gravity = 0
        # player_animation()
        # screen.blit(player_surface, player_rectangle)
        player.draw(screen)
        player.update()

        obsticle_group.draw(screen)
        obsticle_group.update()
        
        # # Obsticle Movement
        # obsticle_rect_list = obsticle_movement(obsticle_rect_list)

        # # Collisions
        game_active = collision_sprite()
        # game_active = collisions(player_rectangle, obsticle_rect_list)



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