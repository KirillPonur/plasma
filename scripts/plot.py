import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Example data
t = np.arange(0.0, 1.0 + 0.01, 0.01)
s = np.cos(4 * np.pi * t) + 2

matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage[utf8x]{inputenc}',
                               r'\usepackage{amsmath}',
                               r'\usepackage{amssymb}']
plt.plot(t, s)

plt.xlabel(r'\textbf{time} (s)')
plt.ylabel(r'\textit{voltage} (mV)',fontsize=16)
plt.title(r"\TeX\ is Number "
          r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
          fontsize=16, color='gray')
# Make room for the ridiculously large title.
plt.subplots_adjust(top=0.8)

# plt.savefig('tex_demo')
plt.show()
# plt.xticks([i for i in range(0,10,1)]) # Х-сетка
# plt.yticks([i for i in range(0,10,1)]) # Y-сетка

# plt.errorbar(x, y, yerr=0.1) #Погрешности
# plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x))) #???
# plt.xlim([0,5]) # Пределы оси
# plt.ylim([0,5]) #


# Надписи
# plt.axvline(21.75,ymin=0, ymax=0.783,color='k', linestyle='--')
#plt.text(21.6, -4,'$\\phi_1$')
# plt.axvline(31,ymin=0, ymax=0.59,color='k', linestyle='--')
# plt.text(31.2, -4,'$\\phi_{min}$')
# plt.axvline(43,ymin=0, ymax=0.93,color='k', linestyle='--')
# plt.text(43.2, -4,'$\\phi_2$')
