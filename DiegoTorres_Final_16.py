import numpy as np

N=1000

T=np.array([73, 28, 59, 52, 39, 137])
X=np.array([4,10,12,80,50,40])
Y=np.array([100,5,80,50,50,200])
sigma=np.ones(6)

def modelo(C, x, y):
	to=C[0]
	xo=C[1]
	yo=C[2]
	vs=C[3]
	t = to + np.sqrt((x-xo)**2+(y-yo)**2)/vs
	return t

def loglikelihood(C):
	tlist=[]
	for i in range(len(T)):
		tlist.append(modelo(C,X[i],Y[i]))
	tlist=np.array(tlist)	
	g=np.zeros(6)
	for i in range(6):
		g[i]=tlist[i]
	d=-0.5*((T-g)/sigma)**2
	d=sum(d)
	return d


A=[]
A.append(10*np.random.random(size=(4,1))-5*np.ones(shape=(4,1)))

for i in range(1,N):
	anterior=A[i-1]
	nuevo=anterior + np.random.normal(loc=0.0, scale=1.0, size=(4,1))
	pantes=loglikelihood(anterior)
	pdespues=loglikelihood(nuevo)
	r=pantes/pdespues
	gamma=np.random.random()
	if(gamma<r):
		A.append(nuevo)
	else:
		A.append(anterior)

		
print(A[-1])
respuesta=np.zeros(4)
for i in range(len(A)):
	respuesta+=np.array(A[i])
	respuesta=respuesta/len(A)
	
print(respuesta)