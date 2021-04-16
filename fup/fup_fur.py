import numpy as np
import matplotlib.pyplot as plt

# число точек
n = 30
k_max = 10
r_max = 10
s_max = 10
fup = np.zeros(n)
m = 1

def my_sinc(x):
    sincd = 1
    for i in range(1,s_max+1):
        sincd= sincd*np.cos(x/(2**i))
    return sincd

def fun_fup(x):
    y = 1/2
    for k in range(1, k_max+1):
        psin = 1
        for r in range(1, r_max+1):
            t = 2*np.pi*k /(m+2)/2**r
            psin = psin*my_sinc(t)
        psin = psin*my_sinc(2*np.pi*k/(m+2)/2)**m*np.cos(2*np.pi*k*x/(m+2))
        y = y+psin
    y = y*2/(m+2)
    return y

for i in range(n):
    x = -(m+2)/2+i*(m+2)/(n-1)
    fup[i] = fun_fup(x)
    print((i+1)/n)

# график
fig = plt.subplots()
x = np.linspace(-(m+2)/2, (m+2)/2, len(fup))
plt.plot(x, fup)
plt.show()
