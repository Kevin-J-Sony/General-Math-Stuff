import numpy as np
import pygame
from jacobian import jacobian
from grid import create_grid, UNIT, PI
from math import sin, cos, sqrt, atan

def pol_to_rect(radius, theta):
    return np.array([radius * cos(theta), radius * sin(theta)])

def rect_to_pol(x,y):
    r = sqrt(x*x + y*y)
    theta = atan(y/x)
    if x < 0:
        theta = theta + PI
    return np.array([r, theta])

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

    grid_width = SCREEN_WIDTH
    grid_height = SCREEN_HEIGHT/2

    # Create the top (input) grid that will serve as the visualization of the domain
    id = np.array([[1,0],[0,1]])
    grid1 = create_grid(id,grid_width,grid_height,(0,0))
    angle = 0
    start = np.array([0, 0])
    origin = np.array([grid_width/2 + 0, grid_height/2 + 0])

    # The points (relative to top grid) which compose the path of the domain
    points = []
    angle = 0.01
    while angle < 4*PI:
        point = np.array([angle*cos(angle)/5,angle*sin(angle)/5])
        points.append(point)
        angle = angle + 0.01

    # The bottom (output) grid that shows the local coordinate change
    jac = 0
    grid2 = 0

    t = 0
    running = True
    flag = False
    while running:
        clock.tick(60)
        screen.fill(BLACK)

        if not flag:
            end = points[t%len(points)]
            jac = jacobian(rect_to_pol,end)
            grid2 = create_grid(jac,grid_width,grid_height,(0, SCREEN_HEIGHT/2)) 
            t += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for line in grid1:
            pygame.draw.line(screen,WHITE,line[0],line[1],LINE_WIDTH)
        for line in grid2:
            pygame.draw.line(screen,WHITE,line[0],line[1],LINE_WIDTH)

        flip = np.array([1,-1])
        for i in range(len(points)):
            p1 = points[i%len(points)] * flip
            p2 = points[(i+1)%len(points)] * flip
            pygame.draw.line(screen,MAGENTA,origin + (UNIT * p1),origin + (UNIT * p2),LINE_WIDTH)
        
        s = UNIT * start * flip
        e = UNIT * end * flip

        pygame.draw.line(screen,MAGENTA,s+origin,e+origin,LINE_WIDTH)
        pygame.display.flip()

        # when space is pressed, flip the flag
        # when i is pressed, get information about current
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            flag = not flag

    pygame.quit()
    

if __name__ == '__main__':
    import pygame
    from math import sin, cos
    main()

