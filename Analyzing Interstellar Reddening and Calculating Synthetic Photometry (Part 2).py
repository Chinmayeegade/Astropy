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
Example 2: Deredden a Spectrum
Dereddening the IUE ultraviolet spectrum and optical photometry of the star ρ Oph (HD 147933).
**This star is famous in the ISM community for having large-RV dust in the line of sight.
"""
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.table import Table
from dust_extinction.parameter_averages import F99
from astroquery.simbad import Simbad
from astroquery.mast import Observations
import astropy.visualization
obsTable = Observations.query_object("HD 147933",radius="1 arcsec")
obsTable_spec=obsTable[obsTable['dataproduct_type']=='spectrum']
obsTable_spec.pprint()
obsids = obsTable_spec[39]['obsid']
dataProductsByID = Observations.get_product_list(obsids)
manifest = Observations.download_products(dataProductsByID)
t_lwr = Table.read('./mastDownload/IUE/lwr05639/lwr05639mxlo_vo.fits')
print(t_lwr)
wav_UV = t_lwr['WAVE'][0,].quantity
UVflux = t_lwr['FLUX'][0,].quantity
custom_query = Simbad()
custom_query.add_votable_fields('fluxdata(U)','fluxdata(B)','fluxdata(V)')
phot_table=custom_query.query_object('HD 147933')
Umag=phot_table['FLUX_U']
Bmag=phot_table['FLUX_B']
Vmag=phot_table['FLUX_V']
wav_U = 0.3660 * u.micron
zeroflux_U_nu = 1.81E-23 * u.Watt/(u.m*u.m*u.Hz)
wav_B = 0.4400 * u.micron
zeroflux_B_nu = 4.26E-23 * u.Watt/(u.m*u.m*u.Hz)
wav_V = 0.5530 * u.micron
zeroflux_V_nu = 3.64E-23 * u.Watt/(u.m*u.m*u.Hz)
zeroflux_U = zeroflux_U_nu.to(u.erg/u.AA/u.cm/u.cm/u.s,
 equivalencies=u.spectral_density(wav_U))
zeroflux_B = zeroflux_B_nu.to(u.erg/u.AA/u.cm/u.cm/u.s,
 equivalencies=u.spectral_density(wav_B))
zeroflux_V = zeroflux_V_nu.to(u.erg/u.AA/u.cm/u.cm/u.s,
 equivalencies=u.spectral_density(wav_V))
Uflux = zeroflux_U * 10.**(-0.4*Umag)
Bflux = zeroflux_B * 10.**(-0.4*Bmag)
Vflux = zeroflux_V * 10.**(-0.4*Vmag)
astropy.visualization.quantity_support()
plt.plot(wav_UV,UVflux,'m',label='UV')
plt.plot(wav_V,Vflux,'ko',label='U, B, V')
plt.plot(wav_B,Bflux,'ko')
plt.plot(wav_U,Uflux,'ko')
plt.legend(loc='best')
plt.ylim(0,3E-10)
plt.title('rho Oph')
plt.show()
Rv = 5.0
Ebv = 0.5
ext = F99(Rv=Rv)
plt.semilogy(wav_UV,UVflux,'m',label='UV')
plt.semilogy(wav_V,Vflux,'ko',label='U, B, V')
plt.semilogy(wav_B,Bflux,'ko')
plt.semilogy(wav_U,Uflux,'ko')
plt.semilogy(wav_UV,UVflux/ext.extinguish(wav_UV,Ebv=Ebv),'b',
 label='dereddened: EBV=0.5, RV=5')
plt.semilogy(wav_V,Vflux/ext.extinguish(wav_V,Ebv=Ebv),'ro',
 label='dereddened: EBV=0.5, RV=5')
plt.semilogy(wav_B,Bflux/ext.extinguish(wav_B,Ebv=Ebv),'ro')
plt.semilogy(wav_U,Uflux/ext.extinguish(wav_U,Ebv=Ebv),'ro')
plt.legend(loc='best')
plt.title('rho Oph')
plt.show()

#Output:Graph of erg / Aᵒ s cm2 vs. Aᵒ

#Credits: Astropy.org