class Node:

    def __init__(self, nodeId, inflow, outflow, volume, relation): 
        self.nodeId = nodeId
        self.inflow = inflow
        self.outflow = outflow
        self.volume = volume
        self.relation = []

    def __repr__(self):
        return str([self.nodeId, self.inflow, self.outflow, self.volume, self.relation])

    def createRelation(self, nodes, relations):
        for i, rela in enumerate(relations):
            self.relation += [Dependencie(self.nodeId, nodes[i].nodeId, rela)]
        print(self.relation)

class Dependencie:

    def __init__(self, depOf, depOn, relation):
        self.depOf = depOf
        self.depOn = depOn
        self.relation = relation

    def __repr__(self):
        return "Node "+ str(self.depOf)+ " has relation "+ str(self.relation)+ " with " + str(self.depOn)
        
class LoadSystem:

    def __init__(self, grid):
        self.nodes = []
        self.createNodes(grid)
        self.insertRelations(grid)

    
    def createNodes(self, grid):
        for i in range(0,len(grid)):
            self.nodes += [Node(i,0,0,0,[])]
    
    def insertRelations(self, grid):
        for i, relas in enumerate(grid):
            self.nodes[i].createRelation(self.nodes, relas)
    

LoadSystem([["+","-","+"],["0","-","+"],["-","-","-"]])