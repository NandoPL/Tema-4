# Soluci贸n del Laboratorio 4
# Problema 4

# Los par谩metros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#######################################################
################# Parte a) ############################
### C y Z variables aleatorias, Omega constante = w ###
#######################################################
# Variables aleatorias C y Z
vaC = stats.norm(5, np.sqrt(0.2))
vaZ = stats.uniform(0, np.pi/2)

# Omega no es Constante aleatoria, sino que una constante w
# w debe estar dentro de 2饾湅(59,1) y 2饾湅(60,1)], por lo que se toma un valor
# dentro del rango
w = 2 * np.pi * 59.6

# Creaci贸n del vector de tiempo
T = 100			# n煤mero de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicializaci贸n del proceso aleatorio X(t) con N realizaciones
N = 10
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creaci贸n de las muestras del proceso x(t) (C y Z independientes)
for i in range(N):
	C = vaC.rvs()
	Z = vaZ.rvs()
	x_t = C * np.cos(w*t + Z)
	X_t[i,:] = x_t
	plt.plot(t, x_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado te贸rico del valor esperado
E = 10/np.pi * (np.cos(w*t) - np.sin(w*t))
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y te贸rico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()



#######################################################
################# Parte b) ############################
### C variable aleatoria, Omega y Z constantes ########
#######################################################

# Variable aleatoria C
vaC = stats.norm(5, np.sqrt(0.2))

# Omega no es Constante aleatoria, sino que una constante w
# Z tamben se vuelve una constante entre 0 y  饾湅/2
w = 2 * np.pi * 59.6
Zb =  np.pi/4

# Angulo theta = constante Zb
theta = Zb


# Creaci贸n de las muestras del proceso x(t) (C independiente)
for i in range(N):
	C = vaC.rvs()
	x_t = C * np.cos(w*t + theta)
	X_t[i,:] = x_t
	#plt.plot(t, x_t)


# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicializaci贸n de matriz de valores de correlaci贸n para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelaci贸n
plt.figure()

# C谩lculo de correlaci贸n para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor te贸rico de correlaci贸n
Rxx = 25.5 * np.cos(w*t + theta) * np.cos(w * (t + taus) + theta)

# Gr谩ficas de correlaci贸n para cada realizaci贸n y la
plt.plot(taus, Rxx, '-.', lw=4, label='Correlaci贸n te贸rica')
plt.title('Funciones de autocorrelaci贸n de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()