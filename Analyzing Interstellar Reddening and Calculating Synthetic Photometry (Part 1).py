"""
Reddening:
Short-wavelength light is extinguished more than long-wavelength light by dust in the Interstellar medium.
Fractional Change to the Flux of Starlight = Optical depth
d Fλ / Fλ = −τ λ
Extinction = 1.086 x Optical Depth
Aλ = 1.086(τ λ)
Hence,
Aλ = −2.5log (Fλ / Fλ ,0)
-----
Example 1: Investigate Extinction Models
*The dust_extinction package provides various models for extinction Aλ normalized to AV .
Programme for displaying a curve graph of (Aλ / AV) vs. wavenumber (λ-1)
"""
import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
from dust_extinction.parameter_averages import CCM89, F99
wav = np.arange(0.1, 3.0, 0.001) * u.micron
for model in [CCM89, F99]:
   for R in (2.0, 3.0, 4.0):
     ext = model(Rv=R)
     plt.plot(1 / wav, ext(wav), label=model.name + ' R=' + str(R))
plt.xlabel('$\lambda^{-1}$ ($\mu$m$^{-1}$)')
plt.ylabel('A($\lambda$) / A(V)')
plt.legend(loc='best')
plt.title('Some Extinction Laws')
plt.show()

#Output: Graph of A(λ0/A(V) vs. wavenumber (λ^-1)

#Credits: Astropy.org