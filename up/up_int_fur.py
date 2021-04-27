import numpy as np
# вычисляет площадь под графиком

# число точек (обязательно нечетное)
n = 101
k_max = 100
m_max = 100
up = np.zeros(n)

def fun_up(x):
    y = 1/2
    for k in range(1, k_max+1):
        psin = 1
        t = np.pi*k /2
        for m in range(1, m_max+1):
            t = t/2
            psin = psin*np.cos(t)**m
        psin = psin*np.cos(np.pi*k*x)
        y = y+psin
    return y

for i in range(n):
    x = -1+i*2/(n-1)
    up[i] = fun_up(x)
    #print((i+1)/n)
s = 0
for i in range(n-1):
    s = s + up[i]+up[i+1]
s = s/(n-1)
print(s)
