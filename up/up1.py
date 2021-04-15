import numpy as np
import matplotlib.pyplot as plt

# число итераций (желательно четное)
n = 8

# число "UP-ов"
k = 11
up1 = np.zeros(1)
up3 = np.zeros(2*len(up1))
up1[0] = 1
for i in range(1, n+1):
    up2 = np.zeros(2*len(up1))
    for j in range(len(up1)):
        up2[j] = up1[j]
        up2[len(up1)+j] = -up1[j]
    up3 = np.zeros(2*len(up1))
    up3[0] = up2[0]
    for j in range(len(up2)-1):
        up3[j+1] = up3[j]+up2[j+1]
    up1 = up3
up = np.zeros(len(up3))
#нормировка
norm = 0
for i in range(1, n-1):
    norm = norm+i
norm = 2**norm
#запись
for i in range(len(up3)-n):
    up[i+int(n/2)] = up3[i]/norm
#разложение
up_1 = np.zeros((k+1)*int(len(up)/2))
for j in range(k):
    for i in range(len(up)):
        s = i+int(len(up)/2)*j
        up_1[s] = up_1[s]+up[i]
# погрешность
p = 0
for i in range(int(len(up)/2), int(len(up_1)-len(up)/2)):
    p = p+abs(up_1[i]-1)
print(p)
# график
fig = plt.subplots()
x = np.linspace(-(k-1)/2-1, (k-1)/2+1, len(up_1))
plt.plot(x, up_1)
plt.show()
