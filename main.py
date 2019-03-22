import copy
import numpy as np

class Node:

    def __init__(self, nodeId, inflow, outflow, volume, relation): 
        self.nodeId = nodeId
        self.inflow = inflow
        self.outflow = outflow
        self.volume = volume
        self.relation = relation

    def __repr__(self):
        return str([self.nodeId, self.inflow, self.outflow, self.volume, self.relation])

class States:
    def __init__(self, nodes, der):
        # Creating a graph with nodes by 2 where the first is the volume
        # and the second is the derivative. "start state"
        self.states = np.zeros((len(nodes.nodes),2),dtype=np.int).tolist()
        self.storedstates = [copy.deepcopy(self.states)]
        self.changeState(nodes,der)
        
    def changeState(self, nodes, der):
        self.states[der][1] = '+'
        while (self.storedstates[-1] != self.states):
            self.storedstates += [copy.deepcopy(self.states)]
            print(self.storedstates)
            self.calcState(nodes)

    def calcState(self, nodes):
        for ind, item in enumerate(self.states):
            if(item[0] == "+"):
                self.reinforceRela(nodes.nodes[ind].relation, nodes)
            elif(item[1] == "+"):
                self.states[ind][0] = "+"

    def reinforceRela(self, relation, nodes):
        for ind, item in enumerate(relation[0]):
            if (item == '+'):
                self.states[ind][1] = "+"

    
    def calcRule(item1,item2):
        if (item1 == '+'):
            if (item2 == '-' or item2 == '?'):
                return '?'
            else:
                return '+'

class LoadSystem:
    # relaGrid is a number of nodes by number of nodes grid reading from 
    # right to up the relations between the nodes. 
    # capGrid is a grid by max inflow min inflow max volume min volume
    def __init__(self, relaGrid):
        self.nodes = []
        self.createNodes(relaGrid)
        for i in range(0, len(self.nodes)):
            States(self,i)

    def createNodes(self, grid):
        for i in range(0,len(grid)):
            nodeI = Node(i,0,0,0,[grid[i]])
            print(nodeI)
            self.nodes += [nodeI]

    

LoadSystem([["0","+","0"],["0","0","0"],["0","+","0"]])