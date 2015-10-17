import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import sys

lectura=str(sys.argv[1])
archivo=np.loadtxt(open(lectura,"r"))

x=archivo[:,0]
y=archivo[:,1]

X="$ "+ str(sys.argv[-2]) + " $"
Y="$ "+ str(sys.argv[-1]) + " $"

#x=np.linspace(0,10,1000)
#y=np.sin(x)

plt.plot(x,y)
plt.xlabel(X,size=20)
plt.ylabel(Y,size=20)
plt.show()
plt.close()






