import pygame
import sys
from random import randint

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
       
       for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(poro_surf, obstacle_rect)
        
       obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

       return obstacle_list
    else: 
        return []

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

bg = pygame.image.load('graphics/bg.png').convert()

# Score surface

# score_surf = test_font.render('Pygame', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

# Obstacles

poro = pygame.image.load('graphics/poro.png').convert_alpha()
poro_surf = pygame.transform.scale(poro, (175,100)).convert_alpha()
poro_rect = poro_surf.get_rect(bottomright = (600,300))

obstacle_rect_list = []



player = pygame.image.load('graphics/player.png').convert_alpha()
player_surf = pygame.transform.scale(player, (75,150)).convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

# Player is at ground
player_gravity = 0

# Intro screen

player_stand = pygame.image.load('graphics/player.png').convert_alpha()

# Attribute rotozoom rotates and then scales the player

player_stand = pygame.transform.rotozoom(player_stand, 0, 0.2)
player_stand_rect = player_stand.get_rect(center = (400,200))


# Velocity of the poro
move_speed = 4

# initial position of the poro
poro_x_pos = 200

# Timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)





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
                        player_gravity = -40
            
            if event.type == pygame.KEYUP:
                print('key up')

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Player jumps when the mouse presses within the rectangle of the player
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    poro_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)
                    
        
                
    
        
        


    # #Checks if user's mouse is down or up
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         print('mouse down')
    
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         print('mouse up')
    # #Checks if user's mouse is moving
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

        pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100))
        # screen.blit(score_surf, score_rect)
        
        poro_rect.x -= move_speed
        
        if poro_rect.x <= 0:
            poro_rect.left = 800

        # Poro changes direction at x = 0

        # if poro_rect.x <= 0:
        #     move_speed = -4
        # if poro_rect.x >= 800:
        #     move_speed = 4
        



        #Keypress = Space

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        screen.blit(poro_surf, poro_rect)


        # Player
        # Gravity
        player_gravity += 1
        # Target player attribute to y-coordinate
        player_rect.y += player_gravity 

        # Creates a floor for the player i.e. the player will remain on the ground at y=300

        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        
        # Obstacle movement
        
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)



        # Collision

        # Game ends when poro touches player
        if poro_rect.colliderect(player_rect):
            game_active = False



        # Player jumps if reaches y-coordinate 400

        # if player_rect.y >= 400:
        #     player_gravity = -40
        #     print('jump!')

        screen.blit(player_surf, player_rect)

        

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
        display_intro()

    if event.type == obstacle_timer and game_active:
        obstacle_rect_list.append(poro_surf.get_rect(bottomright = (randint(900,1100),300)))

    pygame.display.update()
    clock.tick(30)
    



