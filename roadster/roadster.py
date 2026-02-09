import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    v = np.asarray(v)
    return 546.8/v + 50.31 + 0.2584*v + 0.008210*v**2


### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v



### PART 2A ###
def time_to_destination(x, route, n): # x = sträcka, 
    h = x/n
    x = np.linspace(0,x,n+1)
    f = 1/velocity(x,route)
    T = h * (0.5 * f[0] + np.sum(f[1:n]) + 0.5 * f[n])
    return T



### PART 2B ###
def total_consumption(x, route, n):
    h = x/n
    x = np.linspace(0,x,n+1)
    f = consumption(velocity(x,route))
    E = h * (0.5 * f[0] + np.sum(f[1:n]) + 0.5 * f[n])
    
    return E



### PART 3A ###
def distance(T, route):
    """
    Hitta sträcka x där time_to_destination(x) = T.
    Ren Newton-Raphson utan fallback.
    """

    n = 10000000
    distance_array, speed_array = load_route(route)
    X_total = distance_array[-1]

    # Startgissning med medelhastighet
    v_mean = np.mean(speed_array)
    x = v_mean * T
    x = max(0, min(X_total, x))  # håll inom intervallet

    tol = 1e-6
    max_iter = 1000
    n_iter = 0

    while n_iter < max_iter:
        n_iter += 1

        # F(x) = T(x) - T
        f = time_to_destination(x, route, n) - T
        if abs(f) < tol:  # konvergens
            return x

        v = velocity(x, route)

        # Newton-steg
        dx = -f * v  
        x_new = x + dx
        x = x_new

    # Om vi nått max iterationer utan konvergens
    raise RuntimeError("Newton-Raphson konvergerade inte")

### PART 3B ###
def reach(C, route):
    n = 1000000
    distance_array, speed_array = load_route(route)
    x_total = distance_array[-1]

    # Om batteriet räcker hela vägen
    if total_consumption(x_total, route, n) <= C:
        return x_total

    # Startgissning: konstant medelhastighet
    v_mean = np.mean(speed_array)
    x = C / consumption(v_mean)
    x = min(x, x_total)

    tol = 1e-5
    max_iter = 50

    for _ in range(max_iter):
        f = total_consumption(x, route, n) - C
        if abs(f) < tol:
            return x

        df = consumption(velocity(x, route))
        x = x - f / df

        # Säkerhetsklipp
        x = max(0, min(x, x_total))

    raise RuntimeError("Newton-Raphson konvergerade inte")


