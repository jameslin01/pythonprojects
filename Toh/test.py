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



import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('pygamebutton')

font = pygame.font.SysFont('Georgia',40,bold=True)
surf = font.render('Quit', True, 'white')
button = pygame.Rect(200,200,100,60)

while True:
    screen.fill('pink')
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                pygame.quit()
                
    # Checks whether the button is pressed

    a,b = pygame.mouse.get_pos()
    if button.x <= a <= button.x + 100 and button.y <= b <= button.y + 60:
        pygame.draw.rect(screen, (180,180,180), button )
    else:
        pygame.draw.rect(screen, (110, 110, 100), button)

    screen.blit(surf, (button.x +5, button.y+5))
    pygame.display.update()






