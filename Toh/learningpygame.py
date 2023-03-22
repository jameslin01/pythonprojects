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

bg = pygame.image.load('graphics/bg.png')
text = test_font.render('Pygame', False, 'Black')
pole = pygame.image.load(graphics/pole.png)

'''
test_surface1 = pygame.Surface((150,50))
test_surface1.fill('Green')

test_surface2 = pygame.Surface((150,50))
test_surface2.fill('Green')

test_surface3 = pygame.Surface((150,50))
test_surface3.fill('Green')'''


while True:
    screen.fill((0,0,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg,(0,0))
    screen.blit(text, (300,50))

    '''screen.blit(test_surface1, (200,100))
    screen.blit(test_surface2, (300,300))
    screen.blit(test_surface3, (500,300))'''

    #draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)

