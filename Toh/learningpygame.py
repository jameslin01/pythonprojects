import pygame
import sys
from random import randint

# Note: Finish animation the obstacles


# Sprite class for player

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
        player_walk_1 = pygame.transform.scale(player_walk_1, (120, 150))
        player_walk_2 = pygame.image.load('graphics/player_walk_2.png').convert_alpha()
        player_walk_2 = pygame.transform.scale(player_walk_2, (120, 150))
    
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0

        self.player_jump = pygame.image.load('graphics/player_jump.png').convert_alpha()
        self.player_jump = pygame.transform.scale(self.player_jump, (120, 150))

        self.image = self.player_walk[self.player_index]

        self.rect = self.image.get_rect(midbottom = (200, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect. bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

# Sprite class for Obstacle

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'blaze':

            blaze_surf = pygame.image.load('graphics/blaze.png').convert_alpha()
            blaze_surf = pygame.transform.scale(blaze_surf, (50,50))
            y_pos = 50
        else:
            poro = pygame.image.load('graphics/poro.png').convert_alpha()
            poro_surf = pygame.transform.scale(poro, (90,150)).convert_alpha()
            y_pos = 300



        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    # Update function to update frames
    
    def update(self):
        self.animation_state()



def display_score():
    global current_time
    # pygame.time.get_ticks() - start_time resets the time when game restarts

    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render('Score: ' + f'{current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

def display_intro():

    score_surf = test_font.render('Score: ' + f'{score}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,350))
    screen.blit(score_surf, score_rect)

    game_title = test_font.render('Stickman Jump', False, (64,64,64))
    game_title_rect = game_title.get_rect(center = (400,50))
    screen.blit(game_title, game_title_rect)

    instructions = test_font.render('Press Spacebar to play', False, (64,64,64))
    instructions_rect = instructions.get_rect(center = (400, 300))
    screen.blit(instructions, instructions_rect)

def obstacle_movement(obstacle_list):

    if obstacle_list:
       
       # Goes through the obstacles in obstacle_list
       
       for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(poro_surf, obstacle_rect)
            else:
                screen.blit(blaze_surf, obstacle_rect)
        
       obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

       return obstacle_list
    else: 
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index
    
    if player_rect.bottom < 300:
        # jump
        player_surf = player_jump
    
    else:
        # walk
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

    # play walking animation if the player is on the floor
    # display the jump surface when player is not on floor

def player_movement():

    if game_active:
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_rect.x += 10

            if event.key == pygame.K_LEFT:
                player_rect.x -= 10
                        




# Basic setup

pygame.init()
screen = pygame.display.set_mode((800,400))

# Sets title of the window

# pygame.display.set_caption('Pygame')

# Setting the framerate

clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0

# Groups

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


bg = pygame.image.load('graphics/bg.png').convert()

# Score surface

# score_surf = test_font.render('Pygame', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

# Obstacles

# Import enemies

poro = pygame.image.load('graphics/poro.png').convert_alpha()
poro_surf = pygame.transform.scale(poro, (90,150)).convert_alpha()
poro_rect = poro_surf.get_rect(bottomright = (600,300))

blaze_surf = pygame.image.load('graphics/blaze.png').convert_alpha()
blaze_surf = pygame.transform.scale(blaze_surf, (50,50))
blaze_rect = blaze_surf.get_rect(bottomright = (600,300))

obstacle_rect_list = []

# Import Player

player_walk_1 = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
player_walk_1 = pygame.transform.scale(player_walk_1, (120,150))
player_walk_2 = pygame.image.load('graphics/player_walk_2.png').convert_alpha()
player_walk_2 = pygame.transform.scale(player_walk_2, (120,150))
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player_jump.png').convert_alpha()
player_jump = pygame.transform.scale(player_jump, (120,150))
player_surf = pygame.transform.scale(player_walk[player_index], (75,90))
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))

# Player is at ground
player_gravity = 0

# Intro screen

player_stand = pygame.image.load('graphics/player.png').convert_alpha()

# Attribute rotozoom rotates and then scales the player

player_stand = pygame.transform.rotozoom(player_stand, 0, 0.2)
player_stand_rect = player_stand.get_rect(center = (400,200))


# Velocity of the poro
move_speed = 3

# initial position of the poro
poro_x_pos = 200

# Timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)





'''
test_surface1 = pygame.Surface((150,50))
test_surface1.fill('Green')

test_surface2 = pygame.Surface((150,50))
test_surface2.fill('Green')

test_surface3 = pygame.Surface((150,50))
test_surface3.fill('Green')'''


while True:
    
    screen.fill((0,0,0))

    #Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Events for keys
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity = -20
            
            if event.type == pygame.KEYUP:
                print('key up')

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Player jumps when the mouse presses within the rectangle of the player
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom >= 300:
                        player_gravity = -20

            player_movement()

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    # poro_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)
                    
        if event.type == obstacle_timer and game_active:

            if randint(0,2):
                    obstacle_rect_list.append(poro_surf.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(blaze_surf.get_rect(bottomright = (randint(900,1100),100)))
                
    
        
        


    # #Checks if user's mouse is down or up
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         print('mouse down')
    
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         print('mouse up')
    # #Checks where the user's mouse is moving
    #     '''if event.type == pygame.MOUSEMOTION:
    #         print(mouse_pos)
    #     '''
    #     if event.type == pygame.MOUSEMOTION:
    #         if player_rect.collidepoint(event.pos):
    #             print('collision')
    if game_active:
        screen.blit(bg,(0,0))
        # Draws a rectangle

        # pygame.draw.rect(screen, '#c0e8ec', score_rect, )
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

        score = display_score()



        # Draws a line

        # pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 4)

        # Draws an ellipse

        # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100))
        # screen.blit(score_surf, score_rect)
        
        # poro_rect.x -= move_speed
        
        # if poro_rect.x <= 0:
        #     poro_rect.left = 800

        # Poro changes direction at x = 0

        # if poro_rect.x <= 0:
        #     move_speed = -4
        # if poro_rect.x >= 800:
        #     move_speed = 4
        



        # Keypress = Space

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        # screen.blit(poro_surf, poro_rect)


        # Player
        # Gravity
        player_gravity += 1
        # Target player attribute to y-coordinate
        player_rect.y += player_gravity 

        # Creates a floor for the player i.e. the player will remain on the ground at y=300

        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        
        # Obstacle movement
        
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)



        # Collision

        game_active = collisions(player_rect, obstacle_rect_list)

        # Game ends when poro touches player
        # if poro_rect.colliderect(player_rect):
        #     game_active = False



        # Player jumps if reaches y-coordinate 400

        # if player_rect.y >= 400:
        #     player_gravity = -40
        #     print('jump!')

        screen.blit(player_surf, player_rect)
        player.draw(screen)
        player.update()

        

        # screen.blit(test_surface1, (200,100))
        # screen.blit(test_surface2, (300,300))
        # screen.blit(test_surface3, (500,300))

        
        # if player_rect.colliderect(poro_rect):
        #     print('collision')

        
        # mouse_pos = pygame.mouse.get_pos()
        
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())
        


        # draw all our elements
        # update everything
    else:
    
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()

        # Resets player's position after collision

        player_rect.midbottom = (80,300)
        player_gravity = 0

        display_intro()

    

    pygame.display.update()
    clock.tick(30)
    



