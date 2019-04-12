
class State():

    def __init__(self, i):
        self.id = i
        self.quantities = {}
        self.transitions = []
        self.node = None
        self.tooltip = ''
