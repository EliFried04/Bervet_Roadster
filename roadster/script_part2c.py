import numpy as np
import roadster as rsd
import matplotlib.pyplot as plt

# 1. Förberedelser
anna_dist, _ = rsd.load_route('speed_anna')
elsa_dist, _ = rsd.load_route('speed_elsa.npz')

x = anna_dist[-1]  # Slutpunkt Anna
y = elsa_dist[-1]  # Slutpunkt Elsa

# Beräkna referensvärden (I_ref) med ett mycket högt n för att kunna räkna ut felet
n_ref = 10000000
I_refa = rsd.time_to_destination(x, 'speed_anna.npz', n_ref)
I_refe = rsd.time_to_destination(y, 'speed_elsa.npz', n_ref)

# arrays för att få felvärdena
n = 2
värden_a = np.array([])
steg_a = np.array([])
värden_e = np.array([])
steg_e = np.array([])

for i in range(25): #Fler steg ger fler beräkningar men även tydligare att se konvergens
    # Anna
    t_anna = rsd.time_to_destination(x, 'speed_anna.npz', n)
    I_diffa = abs(I_refa - t_anna)
    värden_a = np.append(värden_a, [I_diffa]) 
    steg_a = np.append(steg_a, [n])
    
    # Elsa
    t_elsa = rsd.time_to_destination(y, 'speed_elsa.npz', n)
    I_diffe = abs(I_refe - t_elsa)
    värden_e = np.append(värden_e, [I_diffe]) 
    steg_e = np.append(steg_e, [n])
    
    n = 2 * n

#Plotta figur med fek för elsa och anna + hjälplinjer för de olika konvergens"hastigheterna"
plt.figure(figsize=(10, 6))
plt.loglog(steg_a, värden_a, 'bo-', label='Anna (Empiriskt fel)')
plt.loglog(steg_e, värden_e, 'ro-', label='Elsa (Empiriskt fel)')

#
# Trapetsmetoden bör följa p=2, dvs O(1/n^2) enligt teorin. 
p2 = 2
C_a = värden_a[0] * (steg_a[0]**p2) # Konstant för att lägga linjen rätt
plt.loglog(steg_a, C_a / (steg_a**p2), 'k--', label='Teoretisk O(1/n²)')

# Hjälplinje för p=1 för jämförelse
p1 = 1
C_a1 = värden_a[0] * (steg_a[0]**p1)
plt.loglog(steg_a, C_a1 / (steg_a**p1), 'k:', alpha=0.5, label='Teoretisk O(1/n¹)')

plt.xlabel('Antal delintervall n')
plt.ylabel('Absolut fel')
plt.title('Integrationsfel och noggrannhetsordning')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.show()