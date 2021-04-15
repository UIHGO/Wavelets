import numpy as np
import matplotlib.pyplot as plt
import math

# число "UP-ов"
k = 9

# число точек (обязательно нечетное)
n = 31
k_max = 100
m_max = 100
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

for i in range(n):
    x = -1+i*2/(n-1)
    up[i] = fun_up(x)

up_1 = np.zeros((k+1)*int(len(up)/2)+1)
for j in range(k):
    for i in range(len(up)):
        s = i+int(len(up)/2)*j
        up_1[s] = up_1[s]+up[i]
# погрешность
p = 0
for i in range(int(len(up)/2), int(len(up_1)-len(up)/2)):
    p = p+(up_1[i]-1)**2
print(p)
# график
fig = plt.subplots()
x = np.linspace(-(k-1)/2-1, (k-1)/2+1, len(up_1))
plt.plot(x, up_1)
plt.show()
