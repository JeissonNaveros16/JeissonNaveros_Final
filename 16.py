import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt("monthrg.dat")
anio = d[:,0]
mes = d[:,1]
dia = d[:,2]
manchas = d[:,3]

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

plt.figure(figsize=(15,8))
plt.plot(tiempo, ma)
plt.ylabel("Manchas solares")
plt.xlabel("Timepo(dias)")
plt.savefig("solar.png")