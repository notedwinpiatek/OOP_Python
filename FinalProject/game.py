import pygame
from sys import exit
from random import randint, choice

pygame.init()

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # import player images
        self.player_standing = pygame.image.load('Graphics/Player/player_stand.png').convert_alpha()
        self.player_jump = pygame.image.load('Graphics/Player/jump.png').convert_alpha()
        
        player_walk1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk1,player_walk2]
        
    
        player_flip1 = pygame.transform.flip(player_walk1, True, False)
        player_flip2 = pygame.transform.flip(player_walk2, True, False)
        self.player_walk_flip = [player_flip1,player_flip2]
        
        self.player_jump_flip = pygame.transform.flip(self.player_jump, True, False)
        
        
        self.player_index = 0
        self.player_surface = self.player_walk[self.player_index]
        self.image = self.player_standing
        self.rect = self.image.get_rect(midbottom = (400,562))
        self.player_gravity = 0
        self.moving = False
        self.direction = "right"
        
    def player_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom >= 562:
            self.player_gravity = -20
            
        if key[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 5
            self.walk_animation_left()
            self.moving = True
            self.direction = "left"
        elif key[pygame.K_d] and self.rect.x < 800:
            self.rect.x += 5
            self.walk_animation_right()
            self.moving = True
            self.direction = "right"
        else:
            self.moving = False
    
    def apply_gravity(self):
        self.player_gravity += 1
        self.rect.y += self.player_gravity
        if self.rect.bottom >= 562:
            self.rect.bottom = 562
    
    def jump_animation(self):
        if self.rect.bottom < 562:
            if self.moving and self.direction == "right":
                self.image = self.player_jump
            elif self.moving and self.direction == "left":
                self.image = self.player_jump_flip
    

    
    def walk_animation_right(self):
        self.player_index += 0.2
        if self.player_index >= len(self.player_walk):
            self.player_index = 0
        self.image = self.player_walk[int(self.player_index)]
    
    def walk_animation_left(self):
        self.player_index += 0.2
        if self.player_index >= len(self.player_walk_flip):
            self.player_index = 0
        self.image = self.player_walk_flip[int(self.player_index)]
                
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.jump_animation()
        if not self.moving and self.rect.bottom == 562:
            self.image = self.player_standing
class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        self.platform = pygame.image.load('Graphics/platforms/wood.png').convert_alpha()
# variables
game_active = False
clock = pygame.time.Clock()
main_font = pygame.font.Font('font/Minecraft.ttf', 35)


# Game window
screen = pygame.display.set_mode((800,600))
how_to_play = pygame.image.load('Graphics/how_to_play.png').convert_alpha()
htp_rect = how_to_play.get_rect(topleft = (0,0))

pygame.display.set_caption('Bounce King')

main_text = main_font.render(f'HIT ENTER TO START', False, 'White')
main_rect = main_text.get_rect(center = (400, 300))


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
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_active = True
        
    if game_active:
        # Game window
        screen.fill('#b0ceff')
        screen.blit(ground_surf, ground_rect)
        screen.blit(how_to_play, htp_rect)
        
        # Space Jump
        player.draw(screen)
        player.update()
    else:
        screen.fill('#c0e8ec')
        screen.blit(main_text, main_rect)
    
    
    pygame.display.update()
    clock.tick(60)