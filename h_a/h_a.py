import numpy as np
import math
import matplotlib.pyplot as plt

# порядок функции h_a(x)
a = 3
# число итераций (желательно четное)
n = 10
h1 = np.zeros(1)
h3 = np.zeros(math.ceil(a * len(h1)))
h1[0] = 1
for i in range(1, n+1):
    h2 = np.zeros(math.ceil(a*len(h1)))
    for j in range(len(h1)):
        h2[j] = h2[j]+h1[j]
        q = len(h1)+math.ceil(len(h1)*(a-2))
        h2[j+q] = h2[j+q]-h1[j]
    h3 = np.zeros(math.ceil(a*len(h1)))
    h3[0] = h2[0]
    for j in range(len(h2)-1):
        h3[j+1] = h3[j]+h2[j+1]
    h1 = h3
h = np.zeros(len(h3))
norm = max(h3)/(a/2)

my_file = open("data.txt", "w")

for i in range(len(h3)-n):
    h[i+math.ceil(n/2)] = h3[i]/norm

for i in range(len(h3)):
    my_file.write(str(h[i])+', ')

#график
fig = plt.subplots()
x = np.linspace(-1/(a-1), 1/(a-1), len(h))
plt.plot(x, h)
plt.show()
