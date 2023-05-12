
def square_root(n):
    x = n/2
    for i in range(0,20):
        x = x + (n-x*x)/(2*x)
    return x

if __name__ == '__main__':
    from math import sqrt
    sq1 = square_root(100000001)
    sq2 = sqrt(100000001)

    print(sq1)
    print(sq2)
    print(sq1 - sq2)

    