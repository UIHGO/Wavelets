import numpy as np
import matplotlib.pyplot as plt

# число точек
n = 100
k_max = 150
m_max = 150
up = np.zeros(n)

def fun_up(x):
    y = 1/2
    for k in range(1, k_max+1):
        psin = 1
        t = np.pi*k/2
        for m in range(1, m_max+1):
            t = t/2
            psin = psin*np.cos(t)**m
        psin = psin*np.cos(np.pi*k*x)
        y = y+psin
    return y
#запись
for i in range(n):
    x = -1+i*2/(n-1)
    up[i] = fun_up(x)

# график
fig = plt.subplots()
x = np.linspace(-1, 1, len(up))
plt.plot(x, up)
plt.show()
