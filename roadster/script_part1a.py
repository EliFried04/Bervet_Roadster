#!/usr/bin/env python3
import numpy as np
import roadster
import matplotlib.pyplot as plt

def load_route(filename):
    """
    Laddar data från en .npz-fil och returnerar distans och hastighet.
    """
    with np.load(filename) as data: # Använder context manager för att stänga filen automatiskt
        print(f"Filen '{filename}' innehåller följande arrayer: {data.files}")
        distance = data['distance_km'] # Åtkomst via nyckel
        speed = data['speed_kmph']
        return distance, speed

distance_anna, speed_anna = load_route('speed_anna.npz')
distance_elsa, speed_elsa = load_route('speed_elsa.npz')
speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = roadster.consumption(speed_kmph)

# Punktdiagram Consumption vs Speed
plt.figure()
plt.scatter(speed_kmph, consumption_Whpkm, c='black', s=5)
plt.xlabel('Hastighet [Km/h]')
plt.ylabel('Consumption [Wh/Km]')
plt.title('Consumptions Diagram')
plt.grid(True)
plt.show()



# Punktdiagram ANNA
plt.figure()
plt.scatter(distance_anna, speed_anna, c='black', s=5)
plt.xlabel('Tillryggalagd sträcka [Km]')
plt.ylabel('Hastighet [Km/h]')
plt.title('Annas hastighet')
plt.grid(True)
plt.show()


# Punktdiagram ELSA
plt.figure()
plt.scatter(distance_elsa, speed_elsa, c='black', s=5)
plt.xlabel('Tillryggalagd sträcka [Km]')
plt.ylabel('Hastighet [Km/h]')
plt.title('Elsas hastighet')
plt.grid(True)
plt.show()
