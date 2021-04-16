import numpy as np
import matplotlib.pyplot as plt

# порядок функции up_m(x)
m = 4
# число итераций (желательно четное)
n = 6
up1 = np.zeros(1)
up3 = np.zeros(2*m*len(up1))
up1[0] = 1
for i in range(1, n+1):
    up2 = np.zeros(2*m*len(up1))
    for t in range(m):
        for j in range(len(up1)):
            up2[j+t*len(up1)] = up1[j]
            up2[j+t*len(up1)+len(up1)*m] = -up1[j]
    up3 = np.zeros(2*m*len(up1))
    up3[0] = up2[0]
    for j in range(len(up2)-1):
        up3[j+1] = up3[j]+up2[j+1]
    up1 = up3
up = np.zeros(len(up3))
#нормировка
norm = max(up3)

#my_file = open("data.txt", "w")

for i in range(len(up3)-n):
    up[i+int(n/2)] = up3[i]/norm

#for i in range(len(up3)):
#    my_file.write(str(up[i])+', ')

#площадь
s = 0
for i in range(len(up3)-n-1):
    s = s + up[i]+up[i+1]
s = s/(len(up3)-n-1)
print(s)
