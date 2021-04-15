import numpy as np
import matplotlib.pyplot as plt

n = 14 # число итераций
up1 = np.zeros(1)
up3 = np.zeros(2 * len(up1))
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

# график
fig = plt.subplots()
x = np.linspace(-1, 1, len(up))
plt.plot(x, up)
plt.show()
