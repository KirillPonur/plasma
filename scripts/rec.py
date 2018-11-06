import matplotlib.pylab
from matplotlib.pylab import *
from matplotlib import rc
from functions import parsing
from math import pi
import os.path as path
import sys
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                           r'\usepackage{amsmath}',
                           r'\usepackage{amssymb}'])

rc('font', family='serif')



concentration = path.abspath('..'+'\\scripts\\concentration.txt')
density = path.abspath('..'+'\\scripts\\density.txt')


t, freq1 = parsing(concentration, 1, 0)
r, freq2 = parsing(density, 1, 0)
omegares = array(freq1 * 2 * pi * 10 ** 9)
omegares1 = array(freq2 * 2 * pi * 10 ** 9)

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
print(t, N(omegap))


def f(x):
    # N0 = 1.47*10**12
    # tau0 = 4.4
    # f = N0 * np.exp(-x/tau0)

    N01 = 8.16 * 10**11
    tau01 = 1.072
    N02 = 1.058 * 10**12
    tau02 = 6.0277
    f = N01 * exp(-x / tau01) + N02 * exp(-x / tau02)
    return f



x = linspace(0, t[0], 100)
plot(x, f(x), 'darkblue')
plot(t, N(omegap), 'or')
xlabel(r't, $\text{мc}$', fontsize='16')
ylabel(r'N, $1/\text{см}^{3}$', fontsize='16')
minorticks_on()
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
# plt.savefig('D:/Labs/plasma/fig/decay.pdf')
show()


# # # # plt.subplot(212)
# x = np.linspace(omegap[0], omegap[-1], 100)
# plt.plot(x, N(x), 'darkblue')

# plt.plot(omegap, N(omegap), 'ro')
# plt.xlabel(r'$\omega_p,\text{рад}/\text{с}$', fontsize='16')
# plt.ylabel(r'N, $1/\text{см}^{3}$', fontsize='16')
# plt.minorticks_on()
# plt.grid(which='major', linestyle='-')
# plt.grid(which='minor', linestyle=':')
# plt.savefig('D:/Labs/plasma/fig/concentration.pdf')
# plt.show()


# omegap = (omegares1**2 - omega0res**2)**(1 / 2)
# fig, ax = plt.subplots()
# ax.plot(r, N(omegap), 'ro')
# ax.minorticks_on()
# ax.grid(which='major', linestyle='-')
# ax.grid(which='minor', linestyle=':')
# ax.set_xlabel(r'r, $\text{см}$', fontsize='16')
# ax.set_ylabel(r'N, $1/\text{см}^{3}$', fontsize='16')
# ax.set_ylim(0,6*10**11)
# plt.savefig('D:/Labs/plasma/fig/radial.pdf')
# plt.show()

