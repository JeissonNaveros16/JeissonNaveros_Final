import numpy as np
import matplotlib.pyplot as plt

##prob(data|s)
def prob(x, s):
	return np.exp(-0.5*(x/s)**2)/(s*np.sqrt(2*np.pi))

##prob(s|data)
def likehood(data, s):
	l = 1
	for i in range(len(data)):
		l = l*prob(data[i],s)
	return l

def met_hast(data, n):
	s = [np.random.random()]
	for i in range(1,n):
		p = s[i-1] + np.random.random()-0.5
		r = min(1, likehood(data,p)/likehood(data,s[i-1]))
		a = np.random.random()
		if(a < r):
			s.append(p)
		else:
			s.append(s[i-1])
	return s

d = np.loadtxt("valores.txt")
x = met_hast(d,10**5)

plt.figure(figsize=(15,8))
f, y, t = plt.hist(x, bins=100, density=True)
y1 = (y[:-1] + y[1:])/2
media = np.mean(f*y1)
desviacion = np.std(f*y1)
plt.title("Media de " + str(media) + " y desviación estandar de " + str(desviacion))
plt.ylabel("$prob(\sigma | x_{k})$")
plt.xlabel("$\sigma$")
plt.savefig("sigma.png")