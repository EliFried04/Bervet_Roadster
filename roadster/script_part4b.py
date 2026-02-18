#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import route_nyc 

### Given contour plot ###
n_fine = 100
t_fine = np.linspace(0, 24, n_fine)
x_fine = np.linspace(0, 60, n_fine)
tt_fine, xx_fine = np.meshgrid(t_fine, x_fine)
zz_fine = route_nyc.route_nyc(tt_fine,xx_fine)
w, h = plt.figaspect(0.4)
fig = plt.figure(figsize=(w, h))

# skapa ax lika som i mallen (samma effekt som plt.axes().set_aspect(...))
ax = plt.axes()
ax.set_aspect(0.2, adjustable='box')

cs = ax.contourf(tt_fine, xx_fine, zz_fine, 50, cmap=cm.get_cmap('jet'))
plt.xlabel('Time [hour of day]',fontsize=18)
plt.ylabel('Distance [km]',fontsize=18)
plt.title('Speed [km/h]',fontsize=18)
fig.colorbar(cs)

# ----------------------
# Lägg till: simulera och plotta två rutter med nyc_route_traveler_euler
# ----------------------
# tidssteg i timmar (1 minut)
h_step = 1.0 / 60.0

# Euler-simuleringarna (använder funktionen i route_nyc)
t04, x04, v04 = route_nyc.nyc_route_traveler_euler(4.0, h_step)
t09, x09, v09 = route_nyc.nyc_route_traveler_euler(9.5, h_step)

# plotta kurvorna ovanpå konturen (så att de syns bra mot färgfältet)
ax.plot(t04, x04, linewidth=2.2, color='white', label='Start 04:00')
ax.plot(t09, x09, linewidth=2.2, color='red', label='Start 09:30')

# markera start- och målpositioner
ax.scatter([t04[0]], [x04[0]], color='white', edgecolor='k', zorder=5)
ax.scatter([t09[0]], [x09[0]], color='red', edgecolor='k', zorder=5)
ax.scatter([t04[-1]], [60], color='white', edgecolor='k', zorder=5)
ax.scatter([t09[-1]], [60], color='red', edgecolor='k', zorder=5)

ax.legend(loc='upper right', fontsize=10)
ax.set_xlim(0, 24)
ax.set_ylim(0, 60)

# skriv ut ankomsttider i terminalen (decimal-timmar)
arrival04 = t04[-1]
travel04 = arrival04 - 4.0
arrival09 = t09[-1]
travel09 = arrival09 - 9.5

def hours_to_hm(h):
    hh = int(np.floor(h)) % 24
    mm = int(round((h - np.floor(h)) * 60))
    if mm == 60:
        hh = (hh + 1) % 24
        mm = 0
    return f"{hh:02d}:{mm:02d}"

print("=== Route traveler results ===")
print(f"Start 04:00  -> ankomsttid (decimal h): {arrival04:.6f}  restid: {travel04:.6f} h  ({hours_to_hm(arrival04)})")
print(f"Start 09:30  -> ankomsttid (decimal h): {arrival09:.6f}  restid: {travel09:.6f} h  ({hours_to_hm(arrival09)})")

# Spara precis som i din mall
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')

# visa figuren (behålls interaktivt om du kör lokalt)
plt.show()
