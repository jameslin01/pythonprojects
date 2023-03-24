import pygame
import sys

# Basic setup

pygame.init()
screen = pygame.display.set_mode((800,400))

clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
moves = 0

bg = pygame.image.load('graphics/bg.png').convert()


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


    # Events for keys

    if game_active:
        
        screen.blit(bg, (0,0))

    else:
        
        screen.fill((94, 129, 162))




pygame.display.update()
clock.tick(30)

            
        

