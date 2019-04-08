import pydot

class Graph():

    def __init__(self, states):
        self.graph = pydot.Dot(graph_type='digraph')
        self.states = states
        # self.nodes = [pydot.Node()] * len(self.states)
        self.nodes = []
        self.create_graph()

    def node_desc(self, state):
        s = ''
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
                self.graph.add_edge(pydot.Edge(s.node, t.node)) #, label=self.node_desc(t)))

    def write(self):
        self.graph.write_png('graph.png')
        self.graph.create_svg()
