import pygame
import sys

def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = test_font.render(current_time, False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    print(current_time)



# Basic setup

pygame.init()
screen = pygame.display.set_mode((800,400))

# Sets title of the window

pygame.display.set_caption('Pygame')

# Setting the framerate

clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True

bg = pygame.image.load('graphics/bg.png').convert()

# Score surface

score_surf = test_font.render('Pygame', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

poro = pygame.image.load('graphics/poro.png').convert_alpha()
poro_surf = pygame.transform.scale(poro, (175,100)).convert_alpha()
poro_rect = poro_surf.get_rect(bottomright = (600,300))

player = pygame.image.load('graphics/player.png').convert_alpha()
player_surf = pygame.transform.scale(player, (75,150)).convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

# Player is at ground
player_gravity = 0

# Velocity of the poro
move_speed = 4

# initial position of the poro
poro_x_pos = 200







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
        display_score()
        # Draws a line

        # pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 4)

        # Draws an ellipse

        pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100))
        screen.blit(score_surf, score_rect)
        
        poro_rect.x -= move_speed
        
        if poro_rect.x <= 0:
            move_speed = -4
        if poro_rect.x >= 800:
            move_speed = 4
        



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
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(30)
    



