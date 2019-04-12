#!/usr/local/bin/python3

import argparse
from generate import generate
from clean import clean_states, clean_transitions
from itertools import product
from model import Model
from variables import MagnitudeValues

from graph import Graph

if __name__ == '__main__':

    model = [
            Model("I+", None, "Inflow", "Volume"),
            Model("I-", None, "Outflow", "Volume"),
            Model("P+", None, "Volume", "Outflow"),
            Model("VC", MagnitudeValues.MAX, "Volume", "Outflow"),
            Model("VC", MagnitudeValues.ZERO, "Volume", "Outflow"),
            Model("VC", MagnitudeValues.MAX, "Outflow", "Volume"),
            Model("VC", MagnitudeValues.ZERO, "Outflow", "Volume")
    ]


    parser = argparse.ArgumentParser()
    parser.add_argument('-D', default='./results')
    args = parser.parse_args()

    states = generate()
    new_states = clean_states(states, model)


    transitions = list(product(new_states, new_states))
    new_transitions = clean_transitions(transitions)
    print('new states: {}, old states {}'.format(len(new_states), len(states)))
    print('new transitions: {}, old transitions {}'.format(len(new_transitions), len(transitions)))

    graph = Graph(new_states, path=args.D)
    graph.write()
