import numpy as np
import math
import matplotlib.pyplot as plt


def fact(h):
    fact = 1
    while h > 0:
        fact = fact*h
        h = h-1
    return fact

def c(a,b):
    if (b<0) or (b>a):
        x = 0
    else:
        x= fact(a)
        x = x/fact(b)
        x = x/fact(a-b)
    return  x
# порядок функции fup_n(x)
m = 4
# число итераций (желательно четное)
n = 10
fup1 = np.zeros(m+2)
fup3 = np.zeros(2*len(fup1))
fup1[0] = 1
for i in range(1, n+1):
    fup2 = np.zeros(2*len(fup1))
    for k in range(m+3):
        coefficient = c(m+1,k)-c(m+1,k-1)
        q = k*2**(i-1)
        for j in range(len(fup1)):
            fup2[j+q] = fup2[j+q]+coefficient*fup1[j]
        fup3 = np.zeros(len(fup2))
    fup3[0] = fup2[0]
    for j in range(len(fup2)-1):
        fup3[j+1] = fup3[j]+fup2[j+1]
    fup1 = fup3

fup = np.zeros(len(fup3))

for i in range(len(fup3)-n-m-1):
    fup[i+math.ceil((n+m+1)/2)] = fup3[i]

s = 0
for i in range(len(fup)-1):
    s = s+fup[i]+fup[i+1]
s = s*(m+2)/(len(fup3)-1)/2

for i in range(len(fup3)):
    fup[i] = fup[i]/s
s=0


my_file = open("data.txt", "w")

for i in range(len(fup)):
    my_file.write(str(fup[i])+', ')


# график
fig = plt.subplots()
x = np.linspace(-(m+2)/2, (m+2)/2, len(fup))
plt.plot(x, fup)
plt.show()
