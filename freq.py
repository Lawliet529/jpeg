import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

rapid = np.array([35, 195, 24, 215, 40, 190, 45, 200])
smooth = np.array([125, 137, 140, 152, 155, 167, 170, 182])

fig, ax = plt.subplots(2, 2)

matrix = np.array([rapid])
ax[0, 0].imshow(matrix, cmap="gray", vmin=0, vmax=255)
ax[0, 0].set_xticks([])
ax[0, 0].set_yticks([])
ax[0, 0].set_title("Tần số cao")

interpol = np.linspace(0, 7, 300)
power_smooth = make_interp_spline(np.array(range(8)), rapid)(interpol)
ax[1, 0].plot(interpol, power_smooth)
ax[1, 0].set_xlim(0, 7)
ax[1, 0].set_ylim(0, 255)
ax[1, 0].set_xticks([])
ax[1, 0].plot(np.array(range(8)), rapid, 'o', color='black')

matrix = np.array([smooth])
ax[0, 1].imshow(matrix, cmap="gray", vmin=0, vmax=255)
ax[0, 1].set_xticks([])
ax[0, 1].set_yticks([])
ax[0, 1].set_title("Tần số thấp")

interpol = np.linspace(0, 7, 300)
power_smooth = make_interp_spline(np.array(range(8)), smooth)(interpol)
ax[1, 1].plot(interpol, power_smooth)
ax[1, 1].set_xlim(0, 7)
ax[1, 1].set_ylim(0, 255)
ax[1, 1].set_xticks([])
ax[1, 1].plot(np.array(range(8)), smooth, 'o', color='black')

plt.show()
