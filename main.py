from generate import generate
from clean import clean_states, clean_transitions
from itertools import product
from model import Model
from variables import MagnitudeValues

if __name__ == '__main__':

    model = [
            Model("I+", None, ("Tab", "Inflow"), ("Bathtub", "Volume")),
            Model("I-", None, ("Drain", "Outflow"), ("Bathtub", "Volume")),
            Model("P+", None, ("Container", "Volume"), ("Drain", "Outflow")),
                Model("VC", MagnitudeValues.MAX, ("Container", "Volume"), ("Drain", "Outflow")),
                Model("VC", MagnitudeValues.ZERO, ("Container", "Volume"), ("Drain", "Outflow")),
                Model("VC", MagnitudeValues.MAX, ("Drain", "Outflow"), ("Container", "Volume")),
                Model("VC", MagnitudeValues.ZERO, ("Drain", "Outflow"), ("Container", "Volume"))
        ]


        print('main')
        states = generate()
        new_states = clean_states(states)
        print('new states: {}, old states {}'.format(len(new_states), len(states)))

        transitions = list(product(states, states))
        new_transitions = clean_transitions(transitions)
        print('new transitions: {}, old transitions {}'.format(len(new_transitions), len(transitions)))

