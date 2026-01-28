import numpy as np
import matplotlib.pyplot as plt
import roadster

# === Filnamn för rutterna ===


# === Filnamn för rutterna ===
route_anna = 'speed_anna.npz'
route_elsa = 'speed_elsa.npz'



# =======================
# ===== ANNA ============
# =======================

# Läs in Annas ruttdata
dist_a, speed_a = roadster.load_route('speed_anna.npz')

# Skapa många punkter längs rutten för interpolation
x_anna = np.linspace(dist_a[0], dist_a[-1], 1500)

# Interpolerad hastighet
v_anna = roadster.velocity(x_anna, route_anna)

# Plotta interpolerad funktion
plt.figure()
plt.plot(x_anna, v_anna)
plt.xlabel('Sträcka [Km]')
plt.ylabel('Hastighet [Km/h]')
plt.title('Interpolerad hastighet längs Annas rutt')
plt.grid(True)
plt.show()

# =======================
# ===== ELSA ============
# =======================
# Läs in Elsas ruttdata
dist_e, speed_e = roadster.load_route('speed_elsa.npz')
# Skapa många punkter längs rutten för interpolation
x_e = np.linspace(dist_e[0], dist_e[-1], 1500)

# Interpolerad hastighet
v_e = roadster.velocity(x_e, route_elsa)

# Plotta interpolerad funktion
plt.figure()
plt.plot(x_e, v_e)
plt.xlabel('Sträcka [Km])')
plt.ylabel('Hastighet [Km/h]')
plt.title('Interpolerad hastighet längs Elsas rutt')
plt.grid(True)
plt.show()


# =======================
# Punktdiagram – ANNA
# =======================
plt.figure()
plt.scatter(dist_a, speed_a, c='black', s=5)
plt.xlabel('Sträcka [Km]')
plt.ylabel('Hastighet [Km/h]')
plt.title('Annas hastighet')
plt.grid(True)
plt.show()

# =======================
# Punktdiagram – ELSA
# =======================
plt.figure()
plt.scatter(dist_e, speed_e, c='black', s=5)
plt.xlabel('Sträcka [Km]')
plt.ylabel('Hastighet [Km/h]')
plt.title('Elsas hastighet')
plt.grid(True)
plt.show()