import numpy as np
import matplotlib.pyplot as plt

# число "UP-ов"
k = 9
# число точек
n = 31
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
            t = np.pi*k*(a-1)/a**r
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
#разложение
up_1 = np.zeros((k+1)*int(len(up)/2+1))
for j in range(k):
    for i in range(len(up)):
        s = i+int(len(up)/2)*j
        up_1[s] = up_1[s]+up[i]
# погрешность
p = 0
for i in range(int(len(up)/2), int(len(up_1)-len(up)/2)):
    p = p+(up_1[i]-1)**2
print(p)
#график
fig = plt.subplots()
x = np.linspace(-(k-1)/2, (k-1)/2, len(up_1))
plt.plot(x, up_1)
plt.show()
