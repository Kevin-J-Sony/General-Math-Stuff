import pygame
import numpy as np
from math import sin, cos

# Given a linear map, create a list of pairs of endpoints that represent a line.
# The pair of endpoints will come in the following form: ((start_x, start_y), (end_x, end_y))
# It will NOT be adjusted for the coordinates; however, the grid will be truncated so that
# it can be contained within a box of some width and length
# map: 2 by 2 linear matrix (rows, not columns, are basis vectors)
# width: the width of the grid
# height: the height of the grid
# coord: coordinate of the origin, located relative to grid at width/2, length/2
# 
def create_grid(map, width, height, coord):
    # The unit length is 20 pixels
    UNIT = 20

    # multiply linear map by another linear map that reflects it across the x-axis.
    # however, since im dealing with basis vectors as rows instead of columns
    # this means i have to adjust my calculations likewise
    # the transpose of the reflection matrix is the reflection matrix
    norm_map = np.array([[1,0],[0,-1]])

    # however, the order in which the map is multiplied must reversed
    # map = np.matmul(norm_map,map)
    map = np.matmul(map,norm_map)

    # wrap the origin into a numpy array and get the unit vectors
    origin = np.array([coord[0], coord[1]])
    unit_xaxis = np.array(map[0]) # unit_xaxis = np.array([1,0])
    unit_yaxis = np.array(map[1]) # unit_yaxis = np.array([0,1])

    vertical_lines = []
    adj_width = width/UNIT
    # create vertical lines
    for disp in range(int(-adj_width/2),int(adj_width/2) + 1,1):
        vert_line_bottom = UNIT*(disp * unit_xaxis) - (height/2 * unit_yaxis)
        vert_line_top    = UNIT*(disp * unit_xaxis) + (height/2 * unit_yaxis)

        # Use fact that (A*x)^T = x^T*A^T
        # vert_line_bottom = np.matmul(vert_line_bottom,map)
        # vert_line_top    = np.matmul(vert_line_top,map)

        vert_line_bottom = origin + vert_line_bottom
        vert_line_top    = origin + vert_line_top
        vertical_lines.append((vert_line_bottom, vert_line_top))
    
    horizontal_lines = []
    adj_height = height/UNIT
    # create horizontal lines
    for disp in range(int(-adj_height/2),int(adj_height/2) + 1,1):
        hor_line_left  = UNIT*(disp * unit_yaxis) - (width/2 * unit_xaxis)
        hor_line_right = UNIT*(disp * unit_yaxis) + (width/2 * unit_xaxis)

        # Use fact that (A*x)^T = x^T*A^T
        # hor_line_left  = np.matmul(hor_line_left,map)
        # hor_line_right = np.matmul(hor_line_right,map)


        hor_line_left  = origin + hor_line_left
        hor_line_right = origin + hor_line_right
        horizontal_lines.append((hor_line_left, hor_line_right))
    
    lines = []
    for vl in vertical_lines:
        lines.append(vl)
    for hl in horizontal_lines:
        lines.append(hl)
    # return [(neg_xaxis,pos_xaxis),(neg_yaxis,pos_yaxis)]
    return lines


def main():
    pygame.init()
    SCREEN_WIDTH = SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    WHITE = (255,255,255)
    pygame.display.set_caption("Grid Example")

    # line width 2
    LINE_WIDTH = 2
    
    pi = 3.14159265359
    linear_map = np.array([[cos(pi/6),sin(pi/6)],[-sin(pi/6),cos(pi/6)]]) # basis vectors are encoded as rows instead of columns
    lines = create_grid(linear_map,300,300,(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for line in lines:
            pygame.draw.line(screen,WHITE,line[0],line[1],LINE_WIDTH)
        pygame.display.flip()
    pygame.quit()
    

if __name__ == '__main__':
    main()

