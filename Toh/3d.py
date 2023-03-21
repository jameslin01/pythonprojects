import pygame
import numpy as np

WINDOW_SIZE = 800

window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
clock = pygame.time.Clock()

project_matrix = np.array([[1,0,0],[0,1,0],[0,0,0]])

cube_points = [n for n in range(8)]
cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]
cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[6] = [[1], [1], [-1]]
cube_points[7] = [[-1], [1], [-1]]







# Main Loop

scale = 100

while True:
    clock.tick(60)



    for point in cube_points:

        point_2d = np.multiply(project_matrix, point)

        x = (point_2d[0][0] * scale) * WINDOW_SIZE/2
        y = (point_2d[1][0] * scale) * WINDOW_SIZE/2

        pygame.draw.circle(window, (255,0 ,0), (x,y), 5)
        # first input = colour, second input = position, third input = size


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

