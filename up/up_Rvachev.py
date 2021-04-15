import numpy as np
import math
import matplotlib.pyplot as plt

# число точек
w = 30
n = 10

def fun_up(x, b):
    x = abs(x)
    xx = x
    y = 1
    s = 1
    for k in range(1, n-2):
        bb = 0
        xx = xx*2
        if xx >= 1:  # проверка pk = 1
            xx = xx-1
            xxx = 1
            for j in range(k):
                bbb = b[k-j-1]
                bbb = bbb/math.factorial(k-j-1)
                bbb = bbb/math.factorial(j)
                bbb = bbb*xxx
                bb = bb+bbb
                xxx = xxx*xx
            bbb = 1
            bbb = bbb/math.factorial(k)
            bbb = bbb*xxx
            bb = bb+bbb
            s = -s
            bb = bb*s
            j = k*(k-1)
            j = j/2
            bb = bb/2**j
        y = y+bb
    return y

def init_c(n):
    c = np.zeros(2*n)
    c[0] = 1
    for i in range(1, n):
        c[2*i] = 0
        for j in range(i):
            cc = math.factorial(2*i-2*j+1)
            cc = c[2*j]/cc
            cc = cc*(-1)**(i-j)
            c[2*i] = c[2*i]+cc
        cc = 4**i-1
        c[2*i] = c[2*i]/cc
    return c

def init_a(n, c):
    a = np.zeros(2*n)
    a[0] = 1
    for i in range(1, n):
        aa = c[2*i]
        aa = aa*(-1)**i
        aa = aa*math.factorial(2*i)
        a[2*i] = aa
    return a

def init_b(n, a):
    b = np.zeros(2*n)
    for i in range(1,n):
        bb = 0
        binomials = binom(2*i)
        for j in range(i+1):
            bbb = binomials[2*j]
            bbb = bbb*a[2*j]
            bb = bb+bbb
        bbb = i * 2**(2*i+1)
        bb = bb / bbb
        b[2*i-1] = bb
    for i in range(n):
        b[2*i] = a[2*i]*0.5
    return b

def binom(n):
    binomials_old = np.zeros(1)
    binomials_old = 1
    for i in range(n):
        binomials = np.zeros(i+2)
        binomials[0] = 1
        binomials[i+1] = 1
        for j in range(i):
            binomials[j + 1] = binomials_old[j] + binomials_old[j + 1]
        binomials_old = binomials
    return binomials

b = init_c(int(n/2))
b = init_a(int(n/2), b)
b = init_b(int(n/2), b)
up = np.zeros(w)
for i in range(w):
    x = -1+i*2/(w-1)
    up[i] = fun_up(x, b)
    #print((i+1)/w)

# график
fig = plt.subplots()
x = np.linspace(-1, 1, len(up))
plt.plot(x, up)
plt.show()
