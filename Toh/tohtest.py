import pygame
import sys

# Basic setup

pygame.init()
screen = pygame.display.set_mode((800,400))

clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True
start_time = 0
moves = 0

bg = pygame.image.load('tohgraphics/bg.jpeg').convert()
bg = pygame.transform.scale(bg, (800,400))

board = pygame.Surface((150,50))
board.fill('Gold')


def display_intro():

    game_title = test_font.render('Towers of Hanoi', False, (64,64,64))
    game_title_rect = game_title.get_rect(center = (400,50))
    screen.blit(game_title, game_title_rect)


while True:
    
    screen.fill((64,64,64))

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            pos_surf = test_font.render('Pos: ' + f'{mouse_pos}', False, (64,64,64))
            pos_rect = pos_surf.get_rect(center = (400,350))
            screen.blit(pos_surf, pos_rect)


    # Events for keys

    if game_active:
        
        screen.blit(bg, (0,0))

        pygame.draw.rect(screen, '#c0e8ec', pygame.Rect(80,100,100,80))
    
    else:
        
        screen.fill((94, 129, 162))




    pygame.display.update()

    # Sets the framerate for the game
    clock.tick(30)

            
        

