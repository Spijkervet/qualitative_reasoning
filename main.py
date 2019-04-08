from generate import generate
from clean import clean_states, clean_transitions
from itertools import product
from model import Model
from variables import MagnitudeValues

from graph import Graph

if __name__ == '__main__':

    # model = [
    #         Model("I+", None, "Inflow", "Volume"),
    #         Model("I-", None, "Outflow", "Volume"),
    #         Model("P+", None, "Volume", "Outflow"),
    #         Model("VC", MagnitudeValues.MAX, "Volume", "Outflow"),
    #         Model("VC", MagnitudeValues.ZERO, "Volume", "Outflow"),
    #         Model("VC", MagnitudeValues.MAX, "Outflow", "Volume"),
    #         Model("VC", MagnitudeValues.ZERO, "Outflow", "Volume")
    # ]

    states = generate()
    new_states = clean_states(states)

    print('new states: {}, old states {}'.format(len(new_states), len(states)))

    transitions = list(product(new_states, new_states))
    new_transitions = clean_transitions(transitions)
    print('new transitions: {}, old transitions {}'.format(len(new_transitions), len(transitions)))

    graph = Graph(new_states)
    graph.write()
