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
speed_active = False
start_time = 0
moves = 0
frames_per_second = 10

# Timer

# bg = pygame.image.load('Toh/tohgraphics/bg.jpeg')
bg = pygame.image.load('tohgraphics/bg.jpeg')
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
    return None


def choose_screen():
    
    choose_title = test_font.render('Choose the number of disks', False, (64,64,64))
    choose_title_rect = choose_title.get_rect(center = (400,20))
    screen.blit(choose_title, choose_title_rect)

    return None

speed = [str(i) for i in range(1,11)]

speed_rect = []


def choose_speed():
    
    x, y = 100, 100
    count_x = 0
    global speed_rect
    global chosen_speed

    for numbers in speed:

        if count_x < 3:
            speed_surf = test_font.render(numbers, False, (64,64,64))
            speed_rect = speed_surf.get_rect(center = (x,y))

            if len(num_rect) < 11:
                num_rect.append(speed_rect)

            screen.blit(speed_surf, speed_rect)
            y += 60
            count_x += 1
        else:

            speed_surf = test_font.render(numbers, False, (64,64,64))
            speed_rect = speed_surf.get_rect(center = (x,y))

            if len(num_rect) < 11:
                num_rect.append(speed_rect)
            screen.blit(speed_surf, speed_rect)
            count_x = 0
            x += 200
            y = 100

    return None




def speed_screen():
    
    speed_title = test_font.render('Choose the speed of the animation', False, (64,64,64))
    speed_title_rect = speed_title.get_rect(center = (400,20))
    screen.blit(speed_title, speed_title_rect)
    return None

def draw_Rect(left, top, width, height):

    pygame.draw.rect(screen, 'Cyan', pygame.Rect(left, top, width, height))
    return None
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



index = 0
index_l = 0
index_l1 = 1

count_t1 = len(disks)
count_t2 = 0
count_t3 = 0




def move_disk():
    
    global moves

    global tower1_pos_x
    global tower2_pos_y
    global tower3_pos_y

    global index
    global index_l
  
    global th_1
    global th_2
    global th_3

    global count_t1
    global count_t2
    global count_t3

    global chosen_num

    t1_x = tower1_pos_x 
    t2_x = tower2_pos_x
    t3_x = tower3_pos_x

    th_1 = 325 - 20*chosen_num
    th_2 = 325
    th_3 = 325


    # Centers the disk at a tower
    
    # for i in range(len(disks)):
    if index_l < len(moves_list):
       
        p = int((moves_list[index_l][0])) - 1
        p1 = (moves_list)[index_l][index_l1]

        pos_x, pos_y = disks[p][0].center

        

        if pos_x == t1_x:
            
            wraparound = 1

        if pos_x == t2_x:
            
            wraparound = 0

        if pos_x == t3_x:
            
            wraparound = 2

        if p1 == 'left' and wraparound == 1:

            
            if count_t3 == 0:

                disks[p][0].center = (tower3_pos_x, th_3)

            else:

                disks[p][0].center = (tower3_pos_x, th_3 - 20*count_t3)

                
            count_t1 -= 1
            count_t3 += 1

        if p1 == 'left' and wraparound == 0:

            
            
            if count_t1 == 0:

                disks[p][0].center = (tower1_pos_x, th_1)
            
            
            else:

                
                disks[p][0].center = (tower1_pos_x, th_1 - 20*count_t1)
                
                

            count_t2 -= 1
            count_t1 += 1
           

        if p1 == 'left' and wraparound == 2:

            
            

            if count_t2 == 0:


                disks[p][0].center = (tower2_pos_x, th_2)
               

            else:

                
                disks[p][0].center = (tower2_pos_x, th_2 - 20*count_t2)
                

            count_t3 -= 1
            count_t2 += 1
            

        if p1 == 'right' and wraparound == 1:

           

            if count_t2 == 0:
                

                disks[p][0].center = (tower2_pos_x, th_2)


            else:

                
                
                disks[p][0].center = (tower2_pos_x, th_2 - 20*count_t2)
                
            
            count_t1 -= 1
            count_t2 += 1
            

        if p1 == 'right' and wraparound == 0:

            
            

            if count_t3 == 0:

                
                disks[p][0].center = (tower3_pos_x, th_3)
            

            else:

                
                
                disks[p][0].center = (tower3_pos_x, th_3 - 20*count_t3)
                

            
            count_t2 -= 1
            count_t3 += 1
            

        if p1 == 'right' and wraparound == 2:

            
            

            if count_t1 == 0:
                

                disks[p][0].center = (tower1_pos_x, th_1)
                


            else:

                
                disks[p][0].center = (tower1_pos_x, th_1 - 20*count_t1)
            
                
            count_t3 -= 1
            count_t1 += 1
            
        moves += 1
        index_l += 1


draw_moves = False        
        

while True:

    # The user's choice of number of disks

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(frames_per_second)
        
        if event.type == pygame.MOUSEBUTTONDOWN:          

            if choose_active:
                for i in range(len(num_rect)):

                    # Checks if the mouse clicks collides with any of the numbers

                    if num_rect[i].collidepoint(event.pos):
                        chosen_num = i+1
                        choose_active = False
                        speed_active = True
                        moves_printout(chosen_num)
                        print(moves_list)
                        create_disks()
                        disks.reverse()    
                        num_rect.clear()            
                        break
                    else:
                        choose_active = True
                        
            if not draw_moves and speed_active:

                for i in range(len(num_rect)):

                    if num_rect[i].collidepoint(event.pos):
                        chosen_speed = i+1
                        speed_active = False
                        game_active = True
                        frames_per_second = 10*chosen_speed
                                       
                        break
                    else:
                        speed_active = True

        
                    

    # Events for keys
        
        if not game_active:
            screen.fill((94, 129, 162))
            display_intro()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    choose_active = True



    if game_active:
        
        screen.blit(bg, (0,0))

        num_surf = test_font.render('Moves: ' + f'{moves}', True, (64,64,64))
        num_rect = num_surf.get_rect(center = (400, 50))
        screen.blit(num_surf, num_rect)

        # pygame.draw.rect(screen, '')
        
        screen.blit(board_surf, board_rect)
        screen.blit(tower1_surf, tower1_rect)
        screen.blit(tower2_surf, tower2_rect)
        screen.blit(tower3_surf, tower3_rect)
       
        
        draw_disks()
        move_disk()
        
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
    
    if speed_active:

        screen.fill((94, 129, 162))
        speed_screen()
        choose_speed()

    pygame.display.update()

    # Sets the framerate for the game

    clock.tick(frames_per_second)

        
        


        
            
        





            


