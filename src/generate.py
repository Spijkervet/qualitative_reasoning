
from variables import MagnitudeValues, Magnitude, DerivativeValues, Derivative
from quantity import Quantity
from state import State
from itertools import product


def generate():

    magnitudes = list(map(int, MagnitudeValues))
    derivatives = list(map(int, DerivativeValues))

    state = State(0)
    state.quantities = {
        # ASSUMPTION: Inflow has no MAX
        "Inflow": (magnitudes[:2], derivatives),
        "Volume": (magnitudes, derivatives),
        "Outflow": (magnitudes, derivatives),
    }

    states = []
    temp = []

    for s in state.quantities:
        temp.extend(state.quantities[s])


    prod = product(*temp)
    for p in prod:
        idx = 0
        new_state = State(len(states))
        for s in state.quantities:
            new_state.quantities[s] = {}
            mag_bound = state.quantities[s][0][-1]
            q = Quantity(Magnitude(p[idx], maximum=mag_bound), Derivative(p[idx+1]))
            new_state.quantities[s] = q
            idx += 2
        states.append(new_state)
    return states
