import numpy as np
import matplotlib.pyplot as plt

def X(k, t):
    P = 11
    return P*(t-0)/k + P*(np.exp(-k*(t-0)) - 1)/(k**2)

def dX(k, t):
    P = 11
    return -P*(t-0)/(k**2) - 2*P*(np.exp(-k*(t-0)) - 1)/(k**3) - P*(t-0)*(np.exp(-k*(t-0)))/(k**2)
    # return P*(1-np.exp(-k*(t-0))) / k

def d2X(k, t):
    P=11
    return P - k*dX(k,t)

tT = np.array([0.165, 1.85, 2.81, 3.78, 4.65, 5.50, 6.32, 7.14, 7.96, 8.79, 9.69])
tX = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])



k = 0.5
for j in range(100):
    dS = np.sum(np.array([2*((X(k, tT[i]) - tX[i])) * dX(k, tT[i]) for i in range(len(tT))]))
    d2S = np.array([2*dX(k, tT[i])**2 + 2*(X(k,tT[i]) - tX[i]) * d2X(k, tT[i]) for i in range(len(tT))])
    d2S = np.sum(d2S)
    k = k - dS/d2S
    print(k, '\t', dS)

k = np.array([0.1*i for i in range(-10,10)])
S = np.array([np.sum(
        np.array(
            (X(ki, tT[i]) - tX[i])**2 for i in range(len(tT))
        )
    ) for ki in k])
ki = k[0]
i = 0
S = X(1, 0)
'''
np.array(
        (X(ki, tT[i]) - tX[i])**2 for i in range(len(tT))
    )
    '''

print(S)


plt.plot(tT, tX)
plt.show()


