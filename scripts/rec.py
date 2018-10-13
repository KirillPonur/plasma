import matplotlib.pyplot as plt
from functions import parsing
from math import pi
import numpy as np
plt.rc('text', usetex=True)
plt.rc('text.latex', unicode=True)
plt.rc('text.latex', preamble=[r'\usepackage[utf8x]{inputenc}',
                               r'\usepackage[russian]{babel}',
                               r'\usepackage{amsmath}',
                               r'\usepackage{amssymb}'])

plt.rc('font', family='serif')

concentration = 'D://Labs//plasma//rec//concentration.txt'
density = 'D://Labs//plasma//rec//density.txt'


t, freq1 = parsing(concentration, 1, 0)
r, freq2 = parsing(density, 1, 0)
omegares = np.array(freq1 * 2 * pi * 10 ** 9)
omegares1 = np.array(freq2 * 2 * pi * 10 ** 9)

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


# plt.subplot(211)
plt.plot(t, N(omegap), 'or')
plt.xlabel(r't, $\text{c}$', fontsize='16')
plt.ylabel(r'N, $1/\text{см}^{3}$', fontsize='16')
plt.minorticks_on()
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle=':')
plt.savefig('D:/Labs/plasma/fig/decay.pdf')
plt.show()


# # plt.subplot(212)
x = np.linspace(omegap[0], omegap[-1], 100)
plt.plot(x, N(x), 'c')
plt.plot(omegap, N(omegap), 'ro')
plt.xlabel(r'$\omega_p,\text{рад}/\text{с}$', fontsize='16')
plt.ylabel(r'N, $1/\text{см}^{3}$', fontsize='16')

plt.minorticks_on()
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle=':')
plt.savefig('D:/Labs/plasma/fig/concentration.pdf')
plt.show()


omegap = (omegares1**2 - omega0res**2)**(1 / 2)
fig, ax = plt.subplots()
ax.plot(r, N(omegap), 'r*')
ax.minorticks_on()
ax.grid(which='major', linestyle='-')
ax.grid(which='minor', linestyle=':')
ax.set_xlabel(r'r, $\text{см}$', fontsize='16')
ax.set_ylabel(r'N, $1/\text{см}^{3}$', fontsize='16')
plt.savefig('D:/Labs/plasma/fig/radial.pdf')
plt.show()
