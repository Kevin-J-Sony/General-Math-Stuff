import numpy as np

def f(x, y):
    return (x**2)/20 + (y**2)/20 + np.sin(x) + np.sin(y)

def f2(x):
    return np.sum((x**2)/20 + np.sin(x))

def der(func, x):
    dx = 0.001
    return (func(x+dx) - func(x))/dx

def main():
    np.random.seed(1)
    x = np.random.rand(2)
    print(x)
    print(np.shape(x))

    print(f2(np.array([1,2])))

    gamma = 0.1
    grads = [der(f2, x)]
    for loop in range(100):
        grads.append(der(f2, x))
        momentum = 0
        for i in range(0, len(grads) - 1):
            momentum += 0.8**i * grads[len(grads) - i - 1]
        x = x - gamma * (grads[-1] + momentum) #der(f2, x)
        print(x, '\t', f2(x), '\t', f(x[0], x[1]), '\t', grads[-1])
    


main()

