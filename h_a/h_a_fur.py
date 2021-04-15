import numpy as np
import matplotlib.pyplot as plt

# число точек
n = 30
k_max = 10
r_max = 10
s_max = 10
up = np.zeros(n)
a = 1.25

def my_sinc(x):
    sincd = 1
    for i in range(1,s_max+1):
        sincd= sincd*np.cos(x/(2**i))
    return sincd

def fun_up(x):
    y = 1/2
    for k in range(1, k_max+1):
        psin = 1
        for r in range(1, r_max+1):
            t = np.pi*k * (a-1) / a**r
            psin = psin*my_sinc(t)
        psin = psin*np.cos(np.pi*k*x*(a-1))
        y = y+psin
    y = y*(a-1)
    return y
#запись
for i in range(n):
    x = -1/(a-1)+i*2/(n-1)/(a-1)
    up[i] = fun_up(x)
    print((i+1)/n)
#график
fig = plt.subplots()
x = np.linspace(-1/(a-1), 1/(a-1), len(up))
plt.plot(x, up)
plt.show()
