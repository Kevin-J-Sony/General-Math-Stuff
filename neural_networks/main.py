import matplotlib.pyplot as plt
import matplotlib as mpl
import pygame
from read_numbers import *

# the pixels values contains the pixel value for the images in a 28*28=784 element array
# the values of the pixel range from 0 to 255
# we need to first reverse the order of the array given to properly plot it
# we want to allocate 20 pixels at the very least to each 
def main():
    train_pdata, train_label = read_train_data(5)

    pygame.init()
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Visualizing MNIST dataset")
    clock = pygame.time.Clock()
    UNIT = 20

    running = True
    idx = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_train_data = train_pdata[idx]

        for row in range(28):
            for col in range(28):
                rect = pygame.Rect(col*UNIT+40,row*UNIT+40,UNIT,UNIT)
                shade = current_train_data[row * 28 + col]
                pygame.draw.rect(screen, (shade,shade,shade),rect)


        pygame.display.flip()

        clock.tick(30)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            idx += 1
            idx = idx % 5
            print(train_label[idx])
    pygame.quit()

if __name__ == '__main__':
    main()