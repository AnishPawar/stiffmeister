import numpy as np
import matplotlib.pyplot as plt
apparent = []
actual = np.array([])
# for i in range(-10000,1000):
#     x.append(i/100)
#     y.append(i/100)

# plt.plot(x,y)
# plt.xscale("log")
# plt.show()

for i in range(0,1000):
    apparent.append(i)

j= 5
while j > 0 :
    j -= 1/200
    np.append(actual,j)

np.reshape(actual,(1000))
plt.plot(apparent,actual)
plt.xscale("log")
plt.show()

