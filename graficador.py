import numpy as np
import matplotlib.pyplot as plt

t=np.loadtxt("datos.txt",usecols=0)
x=np.loadtxt("datos.txt",usecols=1)
y=np.loadtxt("datos.txt",usecols=2)

plt.plot(x,y, label='trayectoria')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('TorresDiego_final_15.pdf')