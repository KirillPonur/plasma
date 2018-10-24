import numpy as np
Me = 9.11 * 10**(-28)
Mi = 40 * 1.6 * 10**(-24) - 18 * Me # граммы
qe = 1.6 * 10**(-19)
Te = 5 * qe
R = 1
Vs = np.sqrt( Te / (Mi/1000) )
lambia = R/2
tauN = R**2 / ( 6.2 * Vs**2 * lambia )
tauT = 1.5 * np.sqrt( 2 * np.pi * Mi / Te ) * R / ( 2 + np.log( np.sqrt( Me/Mi ) ) )
print(np.log( np.sqrt( Me/Mi ) ))
print(tauN)