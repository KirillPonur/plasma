import matplotlib.pyplot as plt
from functions import parsing
from math import pi
import numpy as np
# plt.rc('text', usetex=True)
# plt.rc('text.latex', unicode=True)
# plt.rc('text.latex', preamble=r'\\usepackage[utf8]{inputenc}')
# plt.rc('text.latex', preamble=r'\\usepackage[russian]{babel}')
# plt.rc('font', family='serif')

concentration = 'D://Labs//plasma//rec//concentration.txt'
density = 'D://Labs//plasma//rec//density.txt'


t, freq1 = parsing(concentration, 1, 0)
r, freq2 = parsing(density, 1, 0)
omegares = np.array(freq1 * 2 * pi * 10 ** 9)
t = np.array(t)


def N(omegap):
    N = m * omegap**2 / (4 * pi * e**2)
    return N


# print(lam)
# omega-- плазменная частота
# omega0res-- собственная частота резонатора в отсутствии плазмы в рад/с
# Плотность плазмы N
# e-- заряд электрона
# m-- масса электрона
m = 9.10938356 * 10**(-31) * 10**(3)  # CGS
# e = 1.60217662 * 10**(-19) #SI
e = 4.8032 * 10**(-10)
c = 2.99792458 * 10**10  # CGS
l = 1  # CGS
# lam = m * c / (2 * e**2 * 10**17)

omega0res = pi * c / 2 / l
print(omega0res)


omegap = (omegares**2 - omega0res**2)**(1 / 2)


plt.subplot(211)
plt.plot(t, N(omegap), 'o')
plt.xlabel('t')
plt.ylabel('N')
plt.grid(b=True, which='both')
plt.subplot(212)
x = np.linspace(omegap[0], omegap[-1], 100)
plt.plot(x, N(x))
plt.plot(omegap, N(omegap), '.')
plt.xlabel('$\\omega_p$')
plt.ylabel('N')
plt.grid(b=True, which='both')
plt.show()

# omega = (freq2**2 - omega0res**2)**(1 / 2)
# N = m * omega**2 / (4 * pi * e**2)
# plt.plot(r, N, '*')
# plt.show()
