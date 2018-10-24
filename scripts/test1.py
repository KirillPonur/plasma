Me = 9.11 * 10**(-28)
Mi = 40 * 1.6 * 10**(-24) - 18 * Me  # граммы
Te = 5
R = 100
e = 1.6021766 * 10**(-19)
Vs = Te * e / Mi
lambia = R / 2
tauN = R**2 / (6.2 * Vs * lambia)

print(tauN)
