import networkx as nx
from algorithms.prims import Prims

# Testing file to check if the whole program was working porperly

G_one = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)
G_two = nx.read_weighted_edgelist('data/G2.txt', nodetype = int)
G_three = nx.read_weighted_edgelist('data/G3.txt', nodetype = int)

Prims(G_one, 0, True, True)