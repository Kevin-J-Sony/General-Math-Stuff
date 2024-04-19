import matplotlib.pyplot as plt
import matplotlib as mpl
import pygame
from read_numbers import *

def plotter(screen, pdata, label, coord, font):
    # the pixels values contains the pixel value for the images in a 28*28=784 element array
    # the values of the pixel range from 0 to 255
    # we want to allocate 20 pixels at the very least to each 
    UNIT = 20
    for row in range(28):
        for col in range(28):
            rect = pygame.Rect(col*UNIT+coord[0],row*UNIT+coord[1],UNIT,UNIT)
            shade = pdata[row * 28 + col]
            pygame.draw.rect(screen,(shade,shade,shade),rect)

    text = font.render(str(label), True, (255,255,255))
    screen.blit(text, (coord[0], coord[1]))


if __name__ == '__main__':
    train_pdata, train_label = read_train_data(100)

    pygame.init()
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Visualizing MNIST dataset")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 20)

    running = True
    idx = 0
    current_train_data = train_pdata[idx]
    current_label = train_label[idx]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        plotter(screen, current_train_data, current_label, (40, 40), font)

        pygame.display.flip()
        clock.tick(30)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            idx += 1
            idx = idx % 100
            current_train_data = train_pdata[idx]
            current_label = train_label[idx]
        
    pygame.quit()
