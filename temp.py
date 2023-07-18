import pygame

# Define colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (179, 226, 245)
YELLOW = (247, 215, 102)
RED = (219, 86, 86)

# Initialize Pygame
pygame.init()

# Set up the window
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pablo Picasso's Painting")

# Draw the shapes
screen.fill(WHITE)
pygame.draw.rect(screen, LIGHT_BLUE, [50, 50, 300, 300])
pygame.draw.ellipse(screen, YELLOW, [100, 100, 200, 200])
pygame.draw.polygon(screen, RED, [(200, 50), (100, 100), (150, 250), (250, 250), (300, 100)])

# Refresh the screen
pygame.display.flip()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
