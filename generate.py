
from variables import MagnitudeValues, Magnitude, DerivativeValues, Derivative
from quantity import Quantity
from itertools import product

def generate():

    magnitudes = list(map(int, MagnitudeValues))
    derivatives = list(map(int, DerivativeValues))

    system = {
        "Volume": (magnitudes, derivatives),
        # ASSUMPTION: Inflow has no negative magnitude.
        "Inflow": (magnitudes[1:], derivatives),
        "Outflow": (magnitudes, derivatives)
    }

    states = []
    temp = []

    for s in system:
        temp.extend(system[s])


    prod = product(*temp)
    for p in prod:
        idx = 0
        state = {}
        for s in system:
            state[s] = {}
            mag_bound = system[s][0][-1]
            q = Quantity(Magnitude(p[idx], maximum=mag_bound), Derivative(p[idx+1]))
            state[s] = q
            idx += 2
        states.append(state)
    return states
