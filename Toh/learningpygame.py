import pygame
import sys

#Basic setup

pygame.init()
screen = pygame.display.set_mode((800,400))

#Sets title of the window
pygame.display.set_caption('Pygame')
#Setting the framerate
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

bg = pygame.image.load('graphics/bg.png').convert()

#Score surface

score_surf = test_font.render('Pygame', False, 'Black')
score_rect = score_surf.get_rect(center = (400,50))

poro = pygame.image.load('graphics/poro.png').convert_alpha()
poro_surf = pygame.transform.scale(poro, (175,100)).convert_alpha()
poro_rect = poro_surf.get_rect(bottomright = (600,300))

player = pygame.image.load('graphics/player.png').convert_alpha()
player_surf = pygame.transform.scale(player, (75,150)).convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

#initial position of the poro
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


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

    screen.blit(bg,(0,0))
    screen.blit(score_surf, score_rect)
    poro_rect.x -=4
    if poro_rect.right <= 0:
        poro_rect.left = 800
    

    screen.blit(poro_surf, poro_rect)
    screen.blit(player_surf, player_rect)

    # screen.blit(test_surface1, (200,100))
    # screen.blit(test_surface2, (300,300))
    # screen.blit(test_surface3, (500,300))

    
    # if player_rect.colliderect(poro_rect):
    #     print('collision')

    
    # mouse_pos = pygame.mouse.get_pos()
    
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
    


    #draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(30)


