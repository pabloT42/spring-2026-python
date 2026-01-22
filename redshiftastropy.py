from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

import requests
from io import BytesIO
from PIL import Image

SPECTRUM_FITS = "galaxy_spectrum.fits"

RA = 3.992
DEC = -0.303

img_url = (
    "https://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg"
    f"?ra={RA}&dec={DEC}&scale=0.2&width=512&height=512"
    )

response = requests.get(img_url)
response.raise_for_status()

galaxy_img = Image.open(BytesIO(response.content))

#plt.figure(figsize=(5, 5))
#plt.imshow(galaxy_img)
#plt.show()

with fits.open(SPECTRUM_FITS) as hdul:
    data = hdul[1].data
   
mask = (data["restWave"] > 0) & (data["z"] > -100)
d2 = data[mask]

#plt.figure(figsize=(7,4))
#plt. vlines(d2["wave"],0,d2["height"], linewidth=1)
#plt.xlabel("observed wavelength (A)")
#plt.ylabel("Line strength (height)")
#plt.title("Detected Spectral Lines")
#plt.show()


fig, (ax_img, ax_plot) = plt.subplots(1, 2, figsize=(12,5))

ax_img.imshow(galaxy_img)
ax_img.axis("off")
ax_img.set_title("SDSS Galaxy Image")

ax_plot.vlines(d2["wave"], 0, d2["height"], linewidth=1)
ax_plot.set_xlabel("observed wavelength (A)")
ax_plot.set_ylabel("Line strength (height)")
ax_plot.set_title("Detected Spectral Lines")

z_med = float(np.median(d2["z"]))
print("median redshift z =", z_med)
ax_plot.text(
    0.02,0.95, f"Median redshift z + {z_med:.5f}",
    transform=ax_plot.transAxes,
    va="top",
    bbox=dict(boxstyle="round", facecolor = "white", alpha=0.8)
)

plt.tight_layout()
plt.show()
