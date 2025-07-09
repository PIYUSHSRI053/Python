import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as ptl
import numpy as np
x=np.array([10,20,30,40,50,31,24,23,29,44])
y=np.array([0,10,31,41,1,31,25,50,75,100])
ptl.plot(sorted(x),y,c="r",marker='o',linestyle='-',label="Red line")
ptl.title("My First graph")
ptl.xlabel('Over')
ptl.ylabel('Runs')
ptl.grid("True")
ptl.legend()
ptl.show()

# pt.savefif(sys,)

ptl.savefig("p.png")
print("successful")