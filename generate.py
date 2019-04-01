
from variables import MagnitudeValues, Magnitude, DerivativeValues, Derivative
from quantity import Quantity
from itertools import product

def generate():

    magnitudes = list(map(int, MagnitudeValues))
    derivatives = list(map(int, DerivativeValues))

    system = {
        "Bathtub": {
            "Volume": (magnitudes, derivatives)
        },
        "Tab": {
            # ASSUMPTION: Inflow has no negative magnitude.
            "Inflow": (magnitudes[1:], derivatives)
        },
        "Drain": {
            "Outflow": (magnitudes, derivatives)
        }
    }

    states = []
    temp = []

    for s in system:
        for quantity in system[s]:
            print(system[s])
            temp.extend(system[s][quantity])


    prod = product(*temp)
    for p in prod:
        idx = 0
        state = {}
        for s in system:
            state[s] = {}
            for quantity in system[s]:
                mag_bound = system[s][quantity][0][-1]
                q = Quantity(Magnitude(p[idx], maximum=mag_bound), Derivative(p[idx+1]))
                state[s][quantity] = q
                idx += 2
        states.append(state)
    return states
