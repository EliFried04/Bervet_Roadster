import numpy as np
import matplotlib.pyplot as plt
import roadster
import os


# === Hitta mappen där detta script ligger ===
HERE = os.path.dirname(__file__)

# === Filnamn för rutterna ===
route_anna = os.path.join(HERE, 'speed_anna.npz')
route_elsa = os.path.join(HERE, 'speed_elsa.npz')

plt.figure()

# =======================
# ===== ANNA ============
# =======================

# Läs in Annas ruttdata
dist_a, speed_a = roadster.load_route(route_anna)

# Punktdiagram av mätdata (diskreta datapunkter)
plt.plot(dist_a, speed_a, 'o', label='Anna – mätdata')

# Skapa många punkter längs rutten för interpolation
x_anna = np.linspace(dist_a[0], dist_a[-1], 1500)

# Interpolerad hastighet längs rutten
v_anna = roadster.velocity(x_anna, route_anna)

# Plotta interpolerad funktion
plt.plot(x_anna, v_anna, '-', label='Anna – interpolerad hastighet')

# =======================
# ===== ELSA ============
# =======================

# Läs in Elsas ruttdata
dist_e, speed_e = roadster.load_route(route_elsa)

# Punktdiagram av mätdata (diskreta datapunkter)
plt.plot(dist_e, speed_e, 's', label='Elsa – mätdata')

# Skapa många punkter längs rutten för interpolation
x_e = np.linspace(dist_e[0], dist_e[-1], 1500)

# Interpolerad hastighet längs rutten
v_e = roadster.velocity(x_e, route_elsa)

# Plotta interpolerad funktion
plt.plot(x_e, v_e, '--', label='Elsa – interpolerad hastighet')

# === Plot-inställningar ===
plt.xlabel('Tillryggalagd sträcka (km)')
plt.ylabel('Hastighet (km/h)')
plt.title('Hastighet längs rutterna (Anna och Elsa)')
plt.grid(True)
plt.legend()

plt.show()

x_total_anna = dist_a[-1]
a = roadster.time_to_destination(x_total_anna, route_anna, 1000)

print(a, "timmar")
print(a*60, "minuter")

x_total_elsa = dist_e[-1]
b = roadster.time_to_destination(x_total_elsa, route_elsa, 1000)

print(b, "timmar")
print(b*60, "minuter")