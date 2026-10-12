"""
Business application: Flagship-store demand "ripple" map.

Each point on the grid is a location (km east/west and north/south of a
flagship store). The surface height is the weekly sales uplift (% vs. baseline).
Demand oscillates in rings around the store (dense residential rings, dead zones
between them, then the next suburban ring), the same sin(R) shape as the
original gallery example, just with business axes and scaling.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Locations: -5..5 km around the flagship store (0, 0)
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)          # distance from store in km

# Sales uplift (%): +/-12% swing around the store, ring pattern = sin(R)
uplift = 12 * np.sin(R)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, uplift, vmin=uplift.min() * 2, cmap="Blues")

ax.set(xticklabels=[], yticklabels=[], zticklabels=[])
ax.set_title("Weekly sales uplift (%) by distance from flagship store")
fig.savefig("store_demand_ripple.png", dpi=150)

# Business read-out
peak_ring = R[uplift == uplift.max()].mean()
print(f"Strongest demand rings ~{peak_ring:.1f} km from store (+{uplift.max():.1f}%)")
print(f"Weakest rings (dead zones) dip to {uplift.min():.1f}%")
