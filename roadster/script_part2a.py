import roadster as rsd
import matplotlib.pyplot as plt
import numpy as np
#from scipy.integrate import quad

distance_anna, speed_anna = rsd.load_route('speed_anna.npz')
distance_elsa, speed_elsa = rsd.load_route('speed_elsa.npz')

x=distance_anna[-1]
y=distance_elsa[-1]
#t_anna=rsd.time_to_destination(x,'speed_anna.npz',n)
#t_elsa=rsd.time_to_destination(y,'speed_elsa.npz',n)


# referenser, högt n bra
I_refa = rsd.time_to_destination(x,'speed_anna.npz',1000000)


I_refe = rsd.time_to_destination(y,'speed_elsa.npz',1000000)

# svar på tid det tar för elsa och anna
print(f'Tid för Elsa att köra sin rutt: {60* I_refe} minuter, tid för Anna att kköra sin rutt: {I_refa * 60} minuter')


# setup för for loopen, startvärde på n = 2, 
# skulle väl kunna vara högre med tanke på hur grafen för v ser ut
n= 2
värden_a= np.array([])
steg_a = np.array([])
värden_e = np.array([])
steg_e = np.array([])

# for loop där n dubbleras, slutar på n^20 
for i in range(20):

    t_anna=rsd.time_to_destination(x,'speed_anna.npz',n)

    I_diffa= abs(I_refa - t_anna)
    värden_a=np.append(värden_a,[I_diffa]) 
    steg_a = np.append(steg_a,[n])
    t_elsa=rsd.time_to_destination(y,'speed_elsa.npz',n)

    I_diffe= abs(I_refe - t_elsa)
    värden_e=np.append(värden_e,[I_diffe]) 
    steg_e = np.append(steg_e,[n])
    n=2*n





# figur plot + setup 
plt.figure()
plt.loglog(steg_a,värden_a, label = 'Anna')
plt.loglog(steg_e, värden_e, label = 'Elsa')
plt.axhline(y=(1/120), color='r', linestyle='--', label='Gräns: 30s')
plt.xlabel('Antal delintervall (n)')
plt.title('Undersökning delintervall: Tid')
plt.ylabel('Tidsskillnad [h]')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.show()


