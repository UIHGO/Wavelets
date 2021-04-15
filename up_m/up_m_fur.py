import numpy as np
import matplotlib.pyplot as plt

# число точек
n = 50
k_max = 30
r_max = 30
s_max = 30
up = np.zeros(n)
m = 4

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
            t1 = np.pi*k*m/(2*m)**r
            t2 = np.pi*k /(2*m)**r
            psin = psin*my_sinc(t1)**2/my_sinc(t2)
        psin = psin*np.cos(np.pi*k*x)
        y = y+psin
    return y

for i in range(n):
    x = -1+i*2/(n-1)
    up[i] = fun_up(x)
    print((i+1)/n)

# график
fig = plt.subplots()
x = np.linspace(-1, 1, len(up))
plt.plot(x, up)
plt.show()
