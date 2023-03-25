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

bg = pygame.image.load('tohgraphics/bg.jpeg').convert()
bg = pygame.transform.scale(bg, (800,400))

board_surf = pygame.Surface((720,25))
board_surf.fill('#c0e8ec')
board_rect = board_surf.get_rect(center = (400,345))


tower1_surf = pygame.Surface((10,200))
tower1_surf.fill('Silver')
tower1_rect = tower1_surf.get_rect(midbottom = (160, 335))

tower2_surf = pygame.Surface((10,200))
tower2_surf.fill('Silver')
tower2_rect = tower1_surf.get_rect(midbottom = (400, 335))

tower3_surf = pygame.Surface((10,200))
tower3_surf.fill('Silver')
tower3_rect = tower1_surf.get_rect(midbottom = (640, 335))



def display_disks():

    disks = []
    for i in range(1,16):
        for j in range(10,400,20):
        
            disk_surf = test_font.render(i, False, (64,64,64))
            disk_rect = disk_surf.get_rect(center = (320,j))
            screen.blit(disk_surf, disk_rect)
            pygame.draw.rect(screen, 'white', disk_rect, 10)

def choose_screen():
    
    
    choose_title = test_font.render('Choose the number of disks', False, (64,64,64))
    choose_title_rect = choose_title.get_rect(center = (120,20))
    screen.blit(choose_title, choose_title_rect)

        


def display_intro():

    game_title = test_font.render('Towers of Hanoi', False, (64,64,64))
    game_title_rect = game_title.get_rect(center = (400,50))
    screen.blit(game_title, game_title_rect)

    instructions = test_font.render('Press Spacebar to play', False, (64,64,64))
    instructions_rect = instructions.get_rect(center = (400, 300))
    screen.blit(instructions, instructions_rect)


while True:

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    # Events for keys
        
        if game_active:

            if event.type == pygame.KEYUP:
                print('key up')

        else:
            screen.fill((94, 129, 162))
            display_intro()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True


    if game_active:
            
        screen.blit(bg, (0,0))

        # pygame.draw.rect(screen, '')
        
        screen.blit(board_surf, board_rect)
        screen.blit(tower1_surf, tower1_rect)
        screen.blit(tower2_surf, tower2_rect)
        screen.blit(tower3_surf, tower3_rect)

        # Get coordinates based on where your mouse is

        mouse_pos = pygame.mouse.get_pos()
        pos_surf = test_font.render('Pos: ' + f'{mouse_pos}', False, (64,64,64))
        pos_rect = pos_surf.get_rect(center = (400,350))

        if event.type == pygame.MOUSEMOTION:
            screen.blit(pos_surf, pos_rect)
        
    
        
            
        




    pygame.display.update()

    # Sets the framerate for the game

    clock.tick(30)

            
        

