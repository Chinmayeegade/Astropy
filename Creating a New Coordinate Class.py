#Sagittarius Stream to ICRS Coordinate system
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.coordinates import frame_transform_graph
from astropy.coordinates.matrix_utilities import rotation_matrix, matrix_product, matrix_transpose
import astropy.coordinates as coord
import astropy.units as u
class Sagittarius(coord.BaseCoordinateFrame):
    default_representation = coord.SphericalRepresentation
    default_differential = coord.SphericalCosLatDifferential
    frame_specific_representation_info = {
        coord.SphericalRepresentation: [
            coord.RepresentationMapping('lon', 'Lambda'),
            coord.RepresentationMapping('lat', 'Beta'),
            coord.RepresentationMapping('distance', 'distance')]
    }
SGR_PHI = (180 + 3.75) * u.degree # Euler angles (from Law & Majewski 2010)
SGR_THETA = (90 - 13.46) * u.degree
SGR_PSI = (180 + 14.111534) * u.degree
# Generate the rotation matrix using the x-convention (see Goldstein)
D = rotation_matrix(SGR_PHI, "z")
C = rotation_matrix(SGR_THETA, "x")
B = rotation_matrix(SGR_PSI, "z")
A = np.diag([1.,1.,-1.])
SGR_MATRIX = matrix_product(A, B, C, D)
@frame_transform_graph.transform(coord.StaticMatrixTransform, coord.Galactic, Sagittarius)
def galactic_to_sgr():
    """ Compute the transformation matrix from Galactic spherical to
        heliocentric Sgr coordinates.
    """
    return SGR_MATRIX
@frame_transform_graph.transform(coord.StaticMatrixTransform, Sagittarius, coord.Galactic)
def sgr_to_galactic():
    """ Compute the transformation matrix from heliocentric Sgr coordinates to
        spherical Galactic.
    """
    return matrix_transpose(SGR_MATRIX)
icrs = coord.SkyCoord(280.161732*u.degree, 11.91934*u.degree, frame='icrs')
sgr = icrs.transform_to(Sagittarius)
print(sgr)
sgr = coord.SkyCoord(Lambda=np.linspace(0, 2*np.pi, 128)*u.radian,
                     Beta=np.zeros(128)*u.radian, frame='sagittarius')
icrs = sgr.transform_to(coord.ICRS)
print(icrs)
fig, axes = plt.subplots(2, 1, figsize=(8, 10),
                         subplot_kw={'projection': 'aitoff'})
axes[0].set_title("Sagittarius")
axes[0].plot(sgr.Lambda.wrap_at(180*u.deg).radian, sgr.Beta.radian,
             linestyle='none', marker='.')
axes[1].set_title("ICRS")
axes[1].plot(icrs.ra.wrap_at(180*u.deg).radian, icrs.dec.radian,
             linestyle='none', marker='.')
plt.show()
sgr = coord.SkyCoord(Lambda=np.linspace(0, 2*np.pi, 128)*u.radian,
                     Beta=np.zeros(128)*u.radian,
                     pm_Lambda_cosBeta=np.random.uniform(-5, 5, 128)*u.mas/u.yr,
                     pm_Beta=np.zeros(128)*u.mas/u.yr,
                     frame='sagittarius')
icrs = sgr.transform_to(coord.ICRS)
print(icrs)
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
axes[0].set_title("Sagittarius")
axes[0].plot(sgr.Lambda.degree,
             sgr.pm_Lambda_cosBeta.value,
             linestyle='none', marker='.')
axes[0].set_xlabel(r"$\Lambda$ [deg]")
axes[0].set_ylabel(
    fr"$\mu_\Lambda \, \cos B$ [{sgr.pm_Lambda_cosBeta.unit.to_string('latex_inline')}]")
axes[1].set_title("ICRS")
axes[1].plot(icrs.ra.degree, icrs.pm_ra_cosdec.value,
             linestyle='none', marker='.')
axes[1].set_ylabel(
    fr"$\mu_\alpha \, \cos\delta$ [{icrs.pm_ra_cosdec.unit.to_string('latex_inline')}]")
axes[2].set_title("ICRS")
axes[2].plot(icrs.ra.degree, icrs.pm_dec.value,
             linestyle='none', marker='.')
axes[2].set_xlabel("RA [deg]")
axes[2].set_ylabel(
    fr"$\mu_\delta$ [{icrs.pm_dec.unit.to_string('latex_inline')}]")
plt.show()

#Credits: Astropy.org   