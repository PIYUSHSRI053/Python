import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
s=np.array([35,25,15,15,10])
ml=["a","b","c","d","e"]
myexplode=[0.2,0,0,0.1,0]
mycolor=["b","y","hotpink","g","r"]
plt.pie(s,labels=ml,explode=myexplode,shadow=True,colors=mycolor)
plt.legend(title="anything",loc=0)
# plt.show()

plt.savefig("p2.png")
print("successful")


