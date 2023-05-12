import numpy as np


# This function returns the jacobian of a function from R2 to R2 at a given point
def jacobian(function, point):
    dx = dy = 0.001

    # df/dx
    dfx = (function(point[0] + dx, point[1]) - function(point[0], point[1]))/dx

    # df/dy
    dfy = (function(point[0], point[1] + dy) - function(point[0], point[1]))/dy

    return np.array([dfx, dfy])


def main():
    # f(x,y) = [x^2 + xy + y^3,  y^2 + yx + x^3]
    def function(x, y):
        return np.array([x**2+x*y+y**3,y**2+y*x+x**3])
    
    point = (2,1)
    print(jacobian(function,point))

    point = (1,2)
    print(jacobian(function,point))

if __name__ == '__main__':
    main()