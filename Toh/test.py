'''def toh(n, pole_1, pole_3, pole_2):
    if n > 0:
        toh(n - 1, pole_1, pole_2 , pole_3)

        pole_3.append(pole_1.pop())

        toh(n - 1, pole_2, pole_3, pole_1)


num_moves = []

for x in range(1,5):
    A = list(range(x,0,-1))
    B = []
    C = []
    count = 0
    toh(x, A , B , C)
    num_moves.append(count)
print(num_moves)
'''

'''def towerofhanoi(n, source, end, aux):
    if n == 1:
        print("\n Move disk 1 from", source, "to", end)
        return
    towerofhanoi(n-1, source, aux, end)
    print("\n Move disk",str(n), "from", source, "to", end)
    towerofhanoi(n-1, aux, end, source)

n = 3
towerofhanoi(n, 'A', 'C', 'B')'''


#n = number of discs
#left = direction to move pile

# def moves(n, left):
#     '''This function writes the instructions for the towers of Hanoi problem. The recursive
#      function moves() writes the moves needed to move n discs to the left (if left is True) or to the
#      right (if left is False).'''
#     if n == 0: return
#     moves(n-1, not left)
#     if left:
#         print(str(n) + ' left')
#     else:
#         print(str(n) + ' right')
#     moves(n-1, not left)

# n = int(input("Enter the number of discs: "))

# moves(n, True)



# def recursion(n, left):
#     if n == 0: return
#     else:
#         print('Move ' + str(n-1) + ' stack to the right')
#         print('Move ' + str(n) + 'th disc to the left')
#         print('Move ' + str(n-1) + ' stack to the right')

# recursion(3, True)



# import pygame
# pygame.init()

# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('pygamebutton')

# font = pygame.font.SysFont('Georgia',40,bold=True)
# surf = font.render('Quit', True, 'white')
# button = pygame.Rect(200,200,100,60)

# while True:
#     screen.fill('pink')
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             pygame.quit()
#         if events.type == pygame.MOUSEBUTTONDOWN:
#             if button.collidepoint(events.pos):
#                 pygame.quit()
                
#     # Checks whether the button is pressed

#     a,b = pygame.mouse.get_pos()
#     if button.x <= a <= button.x + 100 and button.y <= b <= button.y + 60:
#         pygame.draw.rect(screen, (180,180,180), button )
#     else:
#         pygame.draw.rect(screen, (110, 110, 100), button)

#     screen.blit(surf, (button.x +5, button.y+5))
#     pygame.display.update()


import pygame
pygame.init()

# Set up the game window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Towers of Hanoi")

# Set up the game objects
tower_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
tower_width = 200
tower_height = 400
tower_gap = 100
disk_width = 150
disk_height = 20
num_disks = 5

towers = [[], [], []]
for i in range(num_disks):
    towers[0].append(pygame.Rect(0, 0, disk_width + 20*i, disk_height))
    towers[0][i].centerx = tower_width/2
    towers[0][i].bottom = tower_height
    
base = pygame.Rect(0, 0, tower_width + 2*tower_gap, 10)
base.centerx = screen.get_rect().centerx
base.bottom = tower_height + 10

# Set up the game loop
clock = pygame.time.Clock()
running = True
selected_tower = None
selected_disk = None

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, tower in enumerate(towers):
                if len(tower) > 0 and tower[-1].collidepoint(mouse_pos):
                    selected_tower = i
                    selected_disk = tower.pop()
                    break
            else:
                for i, tower in enumerate(towers):
                    if len(tower) == 0 or tower[-1].width > selected_disk.width:
                        tower.append(selected_disk)
                        selected_tower = None
                        selected_disk = None
                        break
    
    # Draw the game objects
    screen.fill((255, 255, 255))
    
    for i, tower in enumerate(towers):
        rect = pygame.Rect(0, 0, tower_width, tower_height)
        rect.left = i*tower_width + (i+1)*tower_gap
        rect.bottom = tower_height
        pygame.draw.rect(screen, tower_colors[i], rect)
        
        for disk in tower:
            rect = pygame.Rect(0, 0, disk.width, disk.height)
            rect.centerx = tower_width/2 + i*tower_width + (i+1)*tower_gap
            rect.bottom = disk.bottom
            pygame.draw.rect(screen, (0, 0, 0), rect)
            pygame.draw.rect(screen, tower_colors[i], rect, 5)
    
    pygame.draw.rect(screen, (0, 0, 0), base)
    
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(30)

# Clean up the game
pygame.quit()
