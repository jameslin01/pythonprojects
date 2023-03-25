import pygame

# Initialize pygame
pygame.init()

# Set the screen size
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the font for the numbers
font = pygame.font.Font(None, 50)

# Create a list of numbers to display
numbers = [str(i) for i in range(1, 11)]

# Set the position of the first number
x, y = 100, 100

# Loop until the user quits
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on a number
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, number in enumerate(numbers):
                number_width, number_height = font.size(number)
                if x <= mouse_x <= x + number_width and y <= mouse_y <= y + number_height:
                    print(f"You selected {number}")
                    # Remove the selected number from the list
                    numbers.pop(i)
                    break

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the numbers
    for number in numbers:
        text = font.render(number, True, (0, 0, 0))
        screen.blit(text, (x, y))
        y += 60

    # Update the display
    pygame.display.update()

import pygame

pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Set the dimensions of the border
BORDER_WIDTH = 400
BORDER_HEIGHT = 200

# Set the dimensions of the text
TEXT_WIDTH = 200
TEXT_HEIGHT = 50

# Set the font and size of the text
FONT = pygame.font.SysFont('Arial', 36)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Create the border
border_rect = pygame.Rect((WINDOW_WIDTH - BORDER_WIDTH) // 2,
                          (WINDOW_HEIGHT - BORDER_HEIGHT) // 2,
                          BORDER_WIDTH, BORDER_HEIGHT)
border_color = (255, 255, 255)
pygame.draw.rect(window, border_color, border_rect)

# Create the text surface
text_surface = FONT.render('Centered Text', True, (0, 0, 0))

# Create the rectangle to contain the text surface
text_rect = text_surface.get_rect(center=border_rect.center)

# Draw the text surface on the window
window.blit(text_surface, text_rect)

# Update the window
pygame.display.update()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
