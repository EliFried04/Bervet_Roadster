import roadster as rsd
import matplotlib.pyplot as plt
import numpy as np


distance_anna, speed_anna = rsd.load_route('speed_anna.npz')
distance_elsa, speed_elsa = rsd.load_route('speed_elsa.npz')

x=distance_anna[-1]
y=distance_elsa[-1]
#t_anna=rsd.time_to_destination(x,'speed_anna.npz',n)
#t_elsa=rsd.time_to_destination(y,'speed_elsa.npz',n)

print(f'Tid för Elsa att köra sin rutt: {60* I_refe} minuter, tid för Anna att kköra sin rutt: {I_refa * 60} minuter')


# kollar hur många n som behövs för att kunna få rätt minut.


#Skapar referenser som integralerna med kortare steglängd kommer jämföas med för anna och elsa

I_refa = rsd.time_to_destination(x,'speed_anna.npz',100000)

I_refe = rsd.time_to_destination(y,'speed_elsa.npz',100000)

n= 2
värden_a= np.array([])
steg_a = np.array([])
värden_e = np.array([])
steg_e = np.array([])

#dubblar steglängden i slutet av varje iteration för att förhoppnigsvis komma uner gränsen för på minuten

for i in range(11):

    t_anna=rsd.time_to_destination(x,'speed_anna.npz',n)

    I_diffa= abs(I_refa - t_anna)
    värden_a=np.append(värden_a,[I_diffa]) 
    steg_a = np.append(steg_a,[n])
    t_elsa=rsd.time_to_destination(y,'speed_elsa.npz',n)

    I_diffe= abs(I_refe - t_elsa)
    värden_e=np.append(värden_e,[I_diffe]) 
    steg_e = np.append(steg_e,[n])
    n=2*n


plt.figure()
plt.loglog(steg_a,värden_a, label = 'Anna')
plt.loglog(steg_e, värden_e, label = 'Elsa')
plt.axhline(y=(1/120), color='r', linestyle='--', label='Gräns: 30s') # plottar även med streckad linje där 30 sekunder är för att hamnar v under den är vi relativt bra på minuten. 
plt.xlabel('n')
plt.ylabel('tidsskillnad')
plt.grid(True)
plt.show()



