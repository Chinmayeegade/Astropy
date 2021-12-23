"""
dust_extinction package:
Model Flavors
These Models avail the ability to incorporate observed data points and create graphical representation.
Shape Fitting
These models are used to fit the detailed shape of dust extinction curves.
1)FM90 Model
"""
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from dust_extinction.shapes import FM90
fig, ax = plt.subplots()
# generate the curves and plot them
x = np.arange(3.8,11.0,0.1)/u.micron
ext_model = FM90()
ax.plot(x,ext_model(x),label='total')
ext_model = FM90(C3=0.0, C4=0.0)
ax.plot(x,ext_model(x),label='linear term')
ext_model = FM90(C1=0.0, C2=0.0, C4=0.0)
ax.plot(x,ext_model(x),label='bump term')
ext_model = FM90(C1=0.0, C2=0.0, C3=0.0)
ax.plot(x,ext_model(x),label='FUV rise term')
ax.set_xlabel('$x$ [$\mu m^{-1}$]')
ax.set_ylabel('$E(\lambda - V)/E(B - V)$')
ax.set_title('FM90')
ax.legend(loc='best')
plt.tight_layout()
plt.show()
#Output: E(λ-V)/E(B-V) vs. x

"""
2)P92 Model
"""
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from dust_extinction.shapes import P92
fig, ax = plt.subplots()
# generate the curves and plot them
lam = np.logspace(-3.0, 3.0, num=1000)
x = (1.0/lam)/u.micron
ext_model = P92()
ax.plot(1/x,ext_model(x),label='total')
ext_model = P92(FUV_amp=0., NUV_amp=0.0,
                SIL1_amp=0.0, SIL2_amp=0.0, FIR_amp=0.0)
ax.plot(1./x,ext_model(x),label='BKG only')
ext_model = P92(NUV_amp=0.0,
                SIL1_amp=0.0, SIL2_amp=0.0, FIR_amp=0.0)
ax.plot(1./x,ext_model(x),label='BKG+FUV only')
ext_model = P92(FUV_amp=0.,
                SIL1_amp=0.0, SIL2_amp=0.0, FIR_amp=0.0)
ax.plot(1./x,ext_model(x),label='BKG+NUV only')
ext_model = P92(FUV_amp=0., NUV_amp=0.0,
                SIL2_amp=0.0)
ax.plot(1./x,ext_model(x),label='BKG+FIR+SIL1 only')
ext_model = P92(FUV_amp=0., NUV_amp=0.0,
                SIL1_amp=0.0)
ax.plot(1./x,ext_model(x),label='BKG+FIR+SIL2 only')
ext_model = P92(FUV_amp=0., NUV_amp=0.0,
                SIL1_amp=0.0, SIL2_amp=0.0)
ax.plot(1./x,ext_model(x),label='BKG+FIR only')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylim(1e-3,10.)
ax.set_xlabel('$\lambda$ [$\mu$m]')
ax.set_ylabel('$A(x)/A(V)$')
ax.set_title('P92')
ax.legend(loc='best')
plt.tight_layout()
plt.show()
#Output:A(x)/A(V) vs. λ

"""
3)G21 Model
"""
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from dust_extinction.shapes import G21
fig, ax = plt.subplots()
# generate the curves and plot them
lam = np.logspace(np.log10(1.01), np.log10(39.9), num=1000)
x = (1.0/lam)/u.micron
ext_model = G21()
ax.plot(1/x,ext_model(x),label='total')
ext_model = G21(sil1_amp=0.0, sil2_amp=0.0)
ax.plot(1./x,ext_model(x),label='power-law only')
ext_model = G21(sil2_amp=0.0)
ax.plot(1./x,ext_model(x),label='power-law+sil1 only')
ext_model = G21(sil1_amp=0.0)
ax.plot(1./x,ext_model(x),label='power-law+sil2 only')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('$\lambda$ [$\mu$m]')
ax.set_ylabel('$A(x)/A(V)$')
ax.set_title('G21')
ax.legend(loc='best')
plt.tight_layout()
plt.show()
#Output:A(x)/A(V) vs. λ

#Credits: Astropy.org