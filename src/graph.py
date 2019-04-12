import pydot
import os

class Graph():

    def __init__(self, states, path='data'):
        self.graph = pydot.Dot(graph_type='digraph')
        self.states = states
        self.path = path
        # self.nodes = [pydot.Node()] * len(self.states)
        self.nodes = []
        self.create_graph()

    def node_desc(self, state):
        s = 'STATE {}\n'.format(state.id)
        for quantity in state.quantities:
            s += '{}: {}\n'.format(quantity, state.quantities[quantity])
        return s

    def create_graph(self):
        for i, s in enumerate(self.states):
            node = pydot.Node(str(i), label=self.node_desc(s), shape='records')
            self.states[i].node = node
            self.nodes.append(node)
            self.graph.add_node(node)

        self.create_transitions()

    def create_transitions(self):
        for s in self.states:
            for t in s.transitions:
                self.graph.add_edge(pydot.Edge(s.node, t.node, tooltip=s.tooltip)) #, label=self.node_desc(t)))

    def write(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.graph.write_png(os.path.join(self.path, 'graph.png'))

        svg = self.graph.create_svg()
        with open(os.path.join(self.path, 'graph.svg'), 'wb') as s:
            s.write(svg)
