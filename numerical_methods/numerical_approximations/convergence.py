import numpy as np

def f(x):
    return np.sqrt(x**4+1) - np.sqrt(x**4-1)

sum = 0
for i in range(1,7000):
    sum = sum + f(i)
    print(sum, '\t', f(i), '\t', f(i+1)/f(i), '\t', pow(f(i), 1/i))

