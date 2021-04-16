import numpy as np
import matplotlib.pyplot as plt

# число точек
n = 30
k_max = 10
r_max = 10
s_max = 10
fup = np.zeros(n)
m = 3
a = 3

def my_sinc(x):
    sincd = 1
    for i in range(1,s_max+1):
        sincd= sincd * np.cos(x/(2**i))
    return sincd

def fun_fip(x):
    y = 1/2
    l = m + 2 / (a-1)
    for k in range(1, k_max+1):
        psin = 1
        for r in range(1, r_max+1):
            t = 2*np.pi * k /l/ a**r
            psin = psin * my_sinc(t)
        psin = psin * my_sinc(2*np.pi * k /l/2)**m * np.cos(2*np.pi*k*x/l)
        y = y+psin
    y = y * 2/l
    return y

fip=np.zeros(n)

for i in range(n):
    x = -(m/2 + 1/ (a-1))+i*2*(m/2 + 1/ (a-1))/(n-1)
    fip[i] = fun_fip(x)
    print((i+1)/n)

# график
fig = plt.subplots()
x = np.linspace(-(m/2 + 1 / (a-1)), (m/2 + 1 / (a-1)), len(fip))
plt.plot(x, fip)
plt.show()
