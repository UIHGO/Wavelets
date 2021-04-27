import numpy as np
import matplotlib.pyplot as plt

# число точек
n = 30
k_max = 10
r_max = 10
s_max = 10
fup = np.zeros(n)
m = 2

def fun_up(x):
    y = 1/2
    for k in range(1, k_max+1):
        psin = 1
        t = np.pi*k/2
        for r in range(1, r_max+1):
            t = t/2
            psin = psin*np.cos(t)**r
        psin = psin*np.cos(np.pi*k*x)
        y = y+psin
    return y

def fun_fup(x):
    y = fun_up((x-(m+2)/2)/2**m+1)
    y = y*2**(m*(m-1)/2)
    return y

for i in range(n):
    x = m/2+i/(n-1)
    fup[i] = fun_fup(x)
    print((i+1)/n)

# график
fig = plt.subplots()
x = np.linspace(m/2, m/2+1, len(fup))
plt.plot(x, fup)
plt.show()
