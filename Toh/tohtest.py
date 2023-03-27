import pygame
import sys
from functions import *

# Basic setup

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Towers of Hanoi')

clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
choose_active = False
start_time = 0
moves = 0

# Timer

bg = pygame.image.load('Toh/tohgraphics/bg.jpeg').convert()
bg = pygame.transform.scale(bg, (800,400))

board_surf = pygame.Surface((720,25))
board_surf.fill('#c0e8ec')
board_rect = board_surf.get_rect(center = (400,345))

# Tower 1

tower1_surf = pygame.Surface((10,200))
tower1_surf.fill('Silver')
tower1_rect = tower1_surf.get_rect(midbottom = (160, 335))

(tower1_pos_x, tower1_pos_y) = (160, 325)

# Tower 2

tower2_surf = pygame.Surface((10,200))
tower2_surf.fill('Silver')
tower2_rect = tower1_surf.get_rect(midbottom = (400, 335))

(tower2_pos_x, tower2_pos_y) = (400, 325)

# Tower 3

tower3_surf = pygame.Surface((10,200))
tower3_surf.fill('Silver')
tower3_rect = tower1_surf.get_rect(midbottom = (640, 335))

(tower3_pos_x, tower3_pos_y) = (640, 325)

disks_num = [str(i) for i in range(1,17)]

num_rect = []


def display_intro():

    game_title = test_font.render('Towers of Hanoi', False, (64,64,64))
    game_title_rect = game_title.get_rect(center = (400,50))
    screen.blit(game_title, game_title_rect)

    instructions = test_font.render('Press Spacebar to play', False, (64,64,64))
    instructions_rect = instructions.get_rect(center = (400, 300))
    screen.blit(instructions, instructions_rect)


        
def choose_disks():

    x, y = 100, 100
    count_x = 0
    global choose_rect
    global chosen_num

    for numbers in disks_num:

        if count_x < 3:
            choose_surf = test_font.render(numbers, False, (64,64,64))
            choose_rect = choose_surf.get_rect(center = (x,y))

            if len(num_rect) < 17:
                num_rect.append(choose_rect)

            screen.blit(choose_surf, choose_rect)
            y += 60
            count_x += 1
        else:

            choose_surf = test_font.render(numbers, False, (64,64,64))
            choose_rect = choose_surf.get_rect(center = (x,y))

            if len(num_rect) < 17:
                num_rect.append(choose_rect)
            screen.blit(choose_surf, choose_rect)
            count_x = 0
            x += 200
            y = 100



def choose_screen():
    
    choose_title = test_font.render('Choose the number of disks', False, (64,64,64))
    choose_title_rect = choose_title.get_rect(center = (400,20))
    screen.blit(choose_title, choose_title_rect)

def draw_Rect(left, top, width, height):

    pygame.draw.rect(screen, 'Cyan', pygame.Rect(left, top, width, height))

colours = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'blue', 'blueviolet', 'brown', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cyan', 'darkblue', 'orange', 'deeppink']

disks = []

rectangles = []

choose_colour = []


def create_disks():

    global width
    global disk_rect_y
    width = 160
    disk_rect_y = 325

    for count in range(chosen_num):
        rect = pygame.Rect(0,0, width, 20)
        rect.center = (160, disk_rect_y)

        if len(disks) < chosen_num:

            disks.append([rect, colours[count]])
            width -=10
            disk_rect_y -=20


def draw_disks():

    for (disk, colour) in disks:
        pygame.draw.rect(screen, colour, disk)



def move_disk():

    # Centers the disk at a tower
    tower2_pos_y = 325
    for i in range(len(disks)):
        disks[i][0].center = (tower2_pos_x, tower2_pos_y)
        tower2_pos_y -= 20

    for (n, instruction) in moves_list:
        # if instruction == 'left':

        #     disks[int(n)+1][0].move(600, 325)
        # for i in range(2):
        #     disks[int(n)+1][0].move(200, 200)
        disks[0][0].move(10, -20)
        
        
        





while True:

    # The user's choice of number of disks

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if choose_active:
                for i in range(len(num_rect)):

                    # Checks if the mouse clicks collides with any of the numbers

                    if num_rect[i].collidepoint(event.pos):
                        chosen_num = i+1
                        choose_active = False
                        game_active = True
                        moves_printout(chosen_num)
                        print(moves_list)
                        create_disks()
                        disks.reverse()                
                        break
                    else:
                        choose_active = True
                        
                    
                        
        
                    

    # Events for keys
        
        if game_active:

            if event.type == pygame.KEYUP:
                print('key up')
                move_disk()
                print(disks)

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         print(disks)

        else:
            screen.fill((94, 129, 162))
            display_intro()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    choose_active = True



    if game_active:
        
        screen.blit(bg, (0,0))

        num_surf = test_font.render('Number of disks: ' + f'{chosen_num}', True, (64,64,64))
        num_rect = num_surf.get_rect(center = (400, 50))
        screen.blit(num_surf, num_rect)

        # pygame.draw.rect(screen, '')
        
        screen.blit(board_surf, board_rect)
        screen.blit(tower1_surf, tower1_rect)
        screen.blit(tower2_surf, tower2_rect)
        screen.blit(tower3_surf, tower3_rect)
       

        draw_disks()

        # Get coordinates based on where your mouse is

        mouse_pos = pygame.mouse.get_pos()
        pos_surf = test_font.render('Pos: ' + f'{mouse_pos}', False, (64,64,64))
        pos_rect = pos_surf.get_rect(center = (400,350))

        if event.type == pygame.MOUSEMOTION:
            screen.blit(pos_surf, pos_rect)

    if choose_active:
        screen.fill((94, 129, 162))
        choose_screen()
        choose_disks()



        
        


        
            
        




    pygame.display.update()

    # Sets the framerate for the game

    clock.tick(30)

            


