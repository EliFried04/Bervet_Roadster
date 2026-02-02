import numpy as np
import matplotlib.pyplot as plt
import roadster


#rutter
route_anna = 'speed_anna.npz'
route_elsa = 'speed_elsa.npz'

#Anna
# Läs in Annas ruttdata
dist_a, speed_a = roadster.load_route('speed_anna.npz')

#längs rutten för interpolation
x_anna = np.linspace(dist_a[0], dist_a[-1], 1500)

# Interpolerad hastighet
v_anna = roadster.velocity(x_anna, route_anna)

# Plotta interpolerad funktion
plt.figure(1)
plt.plot(x_anna, v_anna, label="Interpolerad funktion")
plt.xlabel('Sträcka [Km]')
plt.ylabel('Hastighet [Km/h]')
plt.title('Interpolerad hastighet längs Annas rutt')
plt.grid(True)

# Punktdiagram anna

plt.scatter(dist_a, speed_a, c='black', s=8, label="Datapunkter")
plt.xlabel('Sträcka [Km]')
plt.ylabel('Hastighet [Km/h]')
plt.title('Annas hastighet')
plt.grid(True)
plt.legend()
plt.show()

# Elsa

# Läs in Elsas ruttdata
dist_e, speed_e = roadster.load_route('speed_elsa.npz')
# Skapa många punkter längs rutten för interpolation
x_e = np.linspace(dist_e[0], dist_e[-1], 1500)

# Interpolerad hastighet
v_e = roadster.velocity(x_e, route_elsa)

# Plotta interpolerad funktion
plt.figure(2)
plt.plot(x_e, v_e, label="Interpolerad funktion")
plt.xlabel('Sträcka [Km])')
plt.ylabel('Hastighet [Km/h]')
plt.title('Interpolerad hastighet längs Elsas rutt')
plt.grid(True)


# Punktdiagram elsa


plt.scatter(dist_e, speed_e, c='black', s=8,label="Datapunkter" )
plt.xlabel('Sträcka [Km]')
plt.ylabel('Hastighet [Km/h]')
plt.title('Elsas hastighet')
plt.grid(True)
plt.legend()
plt.show()


speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = roadster.consumption(speed_kmph)

plt.figure()
plt.plot(speed_kmph, consumption_Whpkm, c='black')
plt.xlabel('Hastighet [Km/h]')
plt.ylabel('Konsumtion [Wh/Km]')
plt.title('Energiförbrukning')
plt.grid(True)
