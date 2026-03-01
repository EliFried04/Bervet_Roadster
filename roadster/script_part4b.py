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
plt.axes().set_aspect(0.2, adjustable='box')
cs = plt.contourf(tt_fine,xx_fine,zz_fine, 50, cmap=cm.get_cmap('jet'))
plt.xlabel('Tid på dagen [h]', fontsize=18)
plt.ylabel('Distans [km]', fontsize=18)
fig.colorbar(cs, label='Hastighet [km/h]')  
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')



ax = plt.gca() 

# 2. Simulera data (samma som förut)
h_step = 1.0 / 60.0
t04, x04, v04 = route_nyc.route_nyc_traveler_euler (4.0, h_step)
t09, x09, v09 = route_nyc.route_nyc_traveler_euler (9.5, h_step)

# 3. Plotta direkt på de hämtade axlarna
# Vi sätter zorder högt för att vara säkra på att de hamnar ovanpå färgfältet
ax.plot(t04, x04, linewidth=2.2, color='black', label='Start 04:00', zorder=10)
ax.plot(t09, x09, linewidth=2.2, color='green', label='Start 09:30', zorder=10)

# Markera start och mål
ax.scatter([t04[0]], [x04[0]], color='black', edgecolor='k', zorder=11)
ax.scatter([t09[0]], [x09[0]], color='green', edgecolor='k', zorder=11)
ax.scatter([t04[-1]], [60], color='black', edgecolor='k', zorder=11)
ax.scatter([t09[-1]], [60], color='green', edgecolor='k', zorder=11)

# 4. Uppdatera legend (valfritt, men hjälper tydligheten)
ax.legend(loc='upper right', fontsize=10)

# 5. Spara igen (nu med linjerna inkluderade)
plt.savefig("speed-data-nyc_with_routes.eps", bbox_inches='tight')

# Visa resultat
plt.show()

arrival04 = t04[-1]
arrival09 = t09[-1]
print(f"Ankomst 04:00: {arrival04:.2f}")
print(f"Ankomst 09:30: {arrival09:.2f}")
