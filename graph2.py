import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30])
y1=np.array([20,40,10])
y2=np.array([40,10,30])
# plt.plot(x, y1, 'r--o', label='Red Line')
plt.bar(x,y2,color='k')
# for x,y in zip(x,y2):
#    plt.plot(x,y,'ro')
plt.title("My First graph")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
# plt.show()

plt.savefig("p1.png")
print("successful")


