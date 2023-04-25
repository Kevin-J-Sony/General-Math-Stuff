import numpy as np
import pygame
from jacobian import jacobian
from grid import create_grid
from math import sin, cos

def pol_to_rect(radius, theta):
    return np.array([radius * cos(theta), radius * sin(theta)])


# for the path traversed, go along a straight ray from the origin until a certain radius is reached

def main():
    pygame.init()
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Path traversal")
    clock = pygame.time.Clock()
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    MAGENTA = (255,0,255)
    LINE_WIDTH = 2

    pi = 3.14159265359

    grid_width = SCREEN_WIDTH
    grid_height = SCREEN_HEIGHT/2

    id = np.array([[1,0],[0,1]])
    grid1 = create_grid(id,grid_width,grid_height,(0,0))
    angle = 0
    radius = 1/1000000    
    start = np.array([radius, angle])
    end = np.array([radius, angle])
    origin = np.array([grid_width/2 + 0, grid_height/2 + 0])

    jac = jacobian(pol_to_rect,end)
    grid2 = create_grid(jac,grid_width,grid_height,(0, SCREEN_HEIGHT/2))

    t = 0
    running = True
    while running:
        clock.tick(30)
        screen.fill(BLACK)

        if t < 500:
            end += np.array([1/100,pi/100])
            jac = jacobian(pol_to_rect,end)
            grid2 = create_grid(jac,grid_width,grid_height,(0, SCREEN_HEIGHT/2)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for line in grid1:
            pygame.draw.line(screen,WHITE,line[0],line[1],LINE_WIDTH)
        for line in grid2:
            pygame.draw.line(screen,WHITE,line[0],line[1],LINE_WIDTH)
        
        pygame.draw.line(screen,MAGENTA,start+origin,end+origin,LINE_WIDTH)
        pygame.display.flip()
        t += 1

    pygame.quit()
    

if __name__ == '__main__':
    import pygame
    from math import sin, cos
    main()

