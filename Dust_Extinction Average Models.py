"""
DUST_EXTINCTION AVERAGE MODELS
dust_extinction package:
Model Flavors
These Models avail the ability to incorporate observed data points and create graphical representation.
Average Models
Milky Way Models:
1)Ultraviolet to Near-infrared:
"""
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from dust_extinction.averages import (GCC09_MWAvg,
                                      B92_MWAvg,
                                      G03_SMCBar,
                                      G03_LMCAvg,
                                      G03_LMC2)
fig, ax = plt.subplots()
# generate the curves and plot them
x = np.arange(0.3,11.0,0.1)/u.micron
models = [GCC09_MWAvg, B92_MWAvg, G03_SMCBar, G03_LMCAvg, G03_LMC2]
for cmodel in models:
   ext_model = cmodel()
   indxs, = np.where(np.logical_and(
      x.value >= ext_model.x_range[0],
      x.value <= ext_model.x_range[1]))
   yvals = ext_model(x[indxs])
   ax.plot(x[indxs], yvals, label=ext_model.__class__.__name__)
ax.set_xlabel('$x$ [$\mu m^{-1}$]')
ax.set_ylabel('$A(x)/A(V)$')
ax.set_title('Ultraviolet to Near-Infrared Models')
ax.legend(loc='best')
plt.tight_layout()
plt.show()

#Output: Graph of A(x)/A(V) vs. x

"""
2)      Near- to Mid-Infrared:
"""
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from dust_extinction.averages import (RL85_MWGC,
                                      RRP89_MWGC,
                                      I05_MWAvg,
                                      CT06_MWLoc,
                                      CT06_MWGC,
                                      F11_MWGC,
                                      G21_MWAvg)
fig, ax = plt.subplots()
# generate the curves and plot them
x = 1.0 / (np.arange(1.0, 40.0 ,0.1) * u.micron)
models = [RL85_MWGC, RRP89_MWGC, I05_MWAvg, CT06_MWLoc, CT06_MWGC,
          F11_MWGC, G21_MWAvg]
for cmodel in models:
  ext_model = cmodel()
  indxs, = np.where(np.logical_and(
     x.value >= ext_model.x_range[0],
     x.value <= ext_model.x_range[1]))
  yvals = ext_model(x[indxs])
  ax.plot(1.0 / x[indxs], yvals, label=ext_model.__class__.__name__)
ax.set_yscale("log")
ax.set_xlabel(r'$\lambda$ [$\mu m$]')
ax.set_ylabel(r'$A(\lambda)/A(V)$')
ax.set_title('Near- to Mid-Infrared Models')
ax.legend(loc='best')
plt.tight_layout()
plt.show()

#Output: Graph of A(λ)/A(V) vs. λ

#Credits: Astropy.org