# Imports

import pygame

# Imports Towers of Hanoi functions from Question 4

from functions import *

# Basic setup 

pygame.init()

# Sets the dimension of the window displayed to be 800 x 400
screen = pygame.display.set_mode((800,400))

pygame.display.set_caption('Towers of Hanoi')

clock = pygame.time.Clock()

# Sets the font of the upcoming texts

test_font = pygame.font.Font(None, 50)

# Intro screen is active at the beginning

game_active = False
choose_active = False
speed_active = False
changed = True
wait = False

# Initial number of moves

moves = 0

# Speed of the animation for the menu screens

frames_per_second = 10

# Creates the board for the towers

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

# Number of disks to display

disks_num = [str(i) for i in range(1,17)]

# List of rectangles each with different positions

num_rect = []

def display_intro():

    '''Function that displays the intro screen before the game starts'''

    # Displays title of the game

    game_title = test_font.render('Towers of Hanoi', False, (64,64,64))
    game_title_rect = game_title.get_rect(center = (400,50))
    
    screen.blit(game_title, game_title_rect)

    # Displays instruction to play the game

    instructions = test_font.render('Press Spacebar to play', False, (64,64,64))
    instructions_rect = instructions.get_rect(center = (400, 300))
    
    screen.blit(instructions, instructions_rect)

    return None

def choose_disks():

    '''Function that displays the choices of disks for Towers of Hanoi'''

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
    
    '''Function that displays the title on the choose screen'''

    choose_title = test_font.render('Choose the number of disks', False, (64,64,64))
    choose_title_rect = choose_title.get_rect(center = (400,20))

    screen.blit(choose_title, choose_title_rect)

    return None

# The available choices for the speed of the animation

speed = [str(i) for i in range(1,11)]

# List of rectangles each with different positions

speed_rect = []

def choose_speed():

    '''Function that displays the choice of the speed of animation'''
    
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
    
    '''Displays the title on the speed screen'''

    speed_title = test_font.render('Choose the speed of the animation', False, (64,64,64))
    speed_title_rect = speed_title.get_rect(center = (400,20))
    
    screen.blit(speed_title, speed_title_rect)

    return None

def draw_Rect(left, top, width, height):

    pygame.draw.rect(screen, 'Cyan', pygame.Rect(left, top, width, height))
    
    return None

# List of up to 16 colours

colours = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'blue', 'blueviolet', 'brown', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cyan', 'darkblue', 'orange', 'deeppink']

# List of disks

disks = []

def create_disks():

    '''Function that creates the rectangles for the disks and puts them all into a list'''

    global width
    global disk_rect_y

    width = 160
    disk_rect_y = 325

    for count in range(chosen_num):

        rect = pygame.Rect(0,0, width, 20)
        rect.center = (160, disk_rect_y)

        if len(disks) < chosen_num:

            disks.append([rect, colours[count], 1])

            width -=10
            disk_rect_y -=20

    return None

def draw_disks():

    '''Function that draws the rectangles on the screen'''

    for (disk, colour, wraparound) in disks:

        pygame.draw.rect(screen, colour, disk)

    return None

# Indexes for the function move_disk()

index_l = 0
index_l1 = 1

# Number of disks in each tower in starting position

count_t1 = len(disks)
count_t2 = 0
count_t3 = 0

def update_object(index, fx, fy, dx, dy):

    '''Function that updates each frame of the disks for a smoother transition'''
    
    global index_l

    global moves

    global changed
    
    global wait

    (rect_x, rect_y) = disks[index][0].center

    pygame.draw.rect(screen, disks[index][1], disks[index][0])

    # Small increments of steps in direction of the destination

    step_x = 0.05*dx
    
    step_y = 0.05*dy

    if index_l < len(moves_list):

        # We are working with vectors here
        
        if disks[index][0].centerx != fx:
            
            disks[index][0].centerx = rect_x + step_x

        if disks[index][0].centery != fy:

            disks[index][0].centery = rect_y + step_y

        # Once the disk has reached its destination we move on to the next disk and increment the number of moves

        if disks[index][0].center == (fx, fy):

            index_l += 1
            moves += 1
            changed = True

            
            
   
def move_disk():
    
    '''Function that provides the foundation for the movement of disks'''

    global moves

    global index_l

    global count_t1
    global count_t2
    global count_t3

    global chosen_num

    global p
    global fx
    global fy
    global dx
    global dy

    # x position of the towers

    t1_x = tower1_pos_x 
    t2_x = tower2_pos_x
    t3_x = tower3_pos_x

    # Initial x position of the disks

    th_1 = 325 - 20*chosen_num
    th_2 = 325
    th_3 = 325

    # Centers the disk at a tower

   
    if index_l < len(moves_list):
       
        p = int((moves_list[index_l][0])) - 1

        p1 = (moves_list)[index_l][index_l1]

        pos_x, pos_y = disks[p][0].center

        # Conditions for wrap around
        
        if pos_x == t1_x:
            
            disks[p][2] = 1

        if pos_x == t2_x:
            
            disks[p][2] = 0

        if pos_x == t3_x:
            
            disks[p][2] = 2

        pos = disks[p][2]

        # Conditions to determine which direction to move the disks based on
        # instruction and wrap around conditions

        if p1 == 'left' and pos == 1:
  
            if count_t3 == 0:

                dx = tower3_pos_x - pos_x

                dy = th_3 - pos_y

                fx = tower3_pos_x

                fy = th_3       

            else:

                dx = tower3_pos_x - pos_x

                dy = th_3 - 20*count_t3 - pos_y

                fx = tower3_pos_x

                fy = th_3 - 20*count_t3

            count_t1 -= 1
            count_t3 += 1

        if p1 == 'left' and pos == 0:

            if count_t1 == 0:

                dx = tower1_pos_x - pos_x

                dy = th_1 - pos_y

                fx = tower1_pos_x

                fy = th_1
            
            else:

                dx = tower1_pos_x - pos_x

                dy = th_1 - 20*count_t1 - pos_y

                fx = tower1_pos_x

                fy = th_1 - 20*count_t1
                 
            count_t2 -= 1
            count_t1 += 1
    
        if p1 == 'left' and pos == 2:

            if count_t2 == 0:
                
                dx = tower2_pos_x - pos_x

                dy = th_2 - pos_y

                fx = tower2_pos_x

                fy = th_2
               
            else:

                dx = tower2_pos_x - pos_x

                dy = th_2 - 20*count_t2 - pos_y

                fx = tower2_pos_x
                
                fy = th_2 - 20*count_t2
                
            count_t3 -= 1
            count_t2 += 1

        if p1 == 'right' and pos == 1:

            if count_t2 == 0:

                dx = tower2_pos_x - pos_x

                dy = th_2 - pos_y

                fx = tower2_pos_x
                
                fy = th_2

            else:

                dx = tower2_pos_x - pos_x

                dy = th_2 - 20*count_t2 - pos_y

                fx = tower2_pos_x

                fy = th_2 - 20*count_t2
            
            count_t1 -= 1
            count_t2 += 1

        if p1 == 'right' and pos == 0:

            if count_t3 == 0:


                dx = tower3_pos_x - pos_x

                dy = th_3 - pos_y

                fx = tower3_pos_x

                fy = th_3
            
            else:

                dx = tower3_pos_x - pos_x

                dy = th_3 - 20*count_t3 - pos_y

                fx = tower3_pos_x

                fy = th_3 - 20*count_t3
                    
            count_t2 -= 1
            count_t3 += 1
     
        if p1 == 'right' and pos == 2:

            if count_t1 == 0:

                dx = tower1_pos_x - pos_x

                dy = th_1 - pos_y

                fx = tower1_pos_x

                fy = th_1

            else:

                dx = tower1_pos_x - pos_x

                dy = th_1 - 20*count_t1 - pos_y

                fx = tower1_pos_x

                fy = th_1 - 20*count_t1
              
            count_t3 -= 1
            count_t1 += 1

# Initially the game is paused

draw_moves = False        
        
while True:

    # The user's choice of number of disks

    # Events

    # Delays the time between each move

    if wait:

        pygame.time.delay(250)
        wait = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    
                    # Starts/stops the game

                    draw_moves = not draw_moves
        
        if event.type == pygame.MOUSEBUTTONDOWN:          

            if choose_active:
                for i in range(len(num_rect)):

                    # Checks if the mouse clicks collides with any of the numbers

                    if num_rect[i].collidepoint(event.pos):

                        chosen_num = i+1

                        choose_active = False
                        speed_active = True

                        moves_printout(chosen_num)
                        create_disks()

                        disks.reverse()    
                        num_rect.clear()     

                        break

                    else:

                        choose_active = True
                        
            if speed_active:

                for i in range(len(num_rect)):

                    # Checks if the mouse clicks collides with any of the numbers

                    if num_rect[i].collidepoint(event.pos):

                        chosen_speed = i+1

                        speed_active = False
                        game_active = True

                        # Changes the speed of the animation according the the user's choice

                        frames_per_second = 10*chosen_speed

                        break
                    
                    else:

                        speed_active = True  

    # Events for keys
        
        # Event to start the game 

        if not game_active and not speed_active:
            screen.fill((94, 129, 162))
            display_intro()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    choose_active = True

    if game_active:

        # Adds captions at the top of the window 

        caption = 'Towers of Hanoi          '
        caption += '(1)  \'Space\' to start or pause    '

        pygame.display.set_caption(caption)

        screen.fill((100,25,60))

        num_surf = test_font.render('Moves: ' + f'{moves}', True, (200,200,200))
        num_rect = num_surf.get_rect(center = (400, 50)
                                     )
        screen.blit(num_surf, num_rect)
        
        screen.blit(board_surf, board_rect)

        screen.blit(tower1_surf, tower1_rect)
        screen.blit(tower2_surf, tower2_rect)
        screen.blit(tower3_surf, tower3_rect)

        draw_disks()
        
    # Allows the animation to be paused/unpaused

    if game_active and draw_moves:

        draw_disks()

        if changed:

            move_disk()
            changed = False
            wait = True


        update_object(p, fx, fy, dx, dy)
        
    # Displays the choices on choose and speed screen

    if choose_active:

        screen.fill((94, 129, 162))
        choose_screen()
        choose_disks()
    
    if speed_active:

        screen.fill((94, 129, 162))
        speed_screen()
        choose_speed()

    # Constant update of animations

    pygame.display.update()

    # Sets the framerate for the game

    clock.tick(frames_per_second)

        
    
