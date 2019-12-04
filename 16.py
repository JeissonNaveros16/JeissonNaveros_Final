import numpy as np
import matplotlib.pyplot as plt

def FT(x):
	N = len(x)
	X = np.zeros(N, dtype=complex)
	for k in range(N):
		X[k] = 0.0j
		for n in range(N):
			X[k] += x[n] * np.exp(-2.0 * np.pi * 1.0j / N ) ** (k * n)
	return X


da = np.loadtxt("monthrg.dat")
anio = da[:,0]
mes = da[:,1]
dia = da[:,2]
manchas = da[:,3]

ii = np.where(anio >= 1900)

a = anio[ii]
me = mes[ii]
d = dia[ii]
ma = manchas[ii]

tiempo = []
for i in range(len(a)):
    temp = a - 1900
    h = temp[i]*365 + me[i]*30 + d[i]
    tiempo.append(h)
    
tiempo = np.array(tiempo)

M = FT(ma)

plt.figure(figsize=(8,15))

plt.subplot(2,1,1)
plt.scatter(np.arange(len(M)), np.abs(M/len(M)))
plt.stem(np.arange(len(M)), np.abs(M/len(M)), use_line_collection=True)
plt.xlabel('k')
plt.ylabel('|$M_k$|/N')
plt.title("N=" + str(len(M)))
plt.grid()

plt.subplot(2,1,2)
plt.plot(tiempo, ma)
plt.title("Manchas solares en función del tiempo")
plt.ylabel("Manchas")
plt.xlabel("Tiempo(dias)")

plt.savefig("solar.png")