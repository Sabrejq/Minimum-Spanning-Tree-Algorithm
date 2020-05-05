"""
Julio Quintero 5/6/2020

Final Project Outline: MST Python Package
CS 1311: Intro. To Computation with Python

"""

import networkx as nx
from algorithms.prims import Prims

# Variables saving data from files G1, G2, and G3 to then by passed to Prims
G_one = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)
G_two = nx.read_weighted_edgelist('data/G2.txt', nodetype = int)
G_three = nx.read_weighted_edgelist('data/G3.txt', nodetype = int)

"""
Prims Function that solves MTS. Arguemnts 1 is the variables declare above. 
Arguemnt two is which from which node the function will start. Argurmnt 3 is 
if a graph will be drawn. Arguemnt 4 is if info for the graph is to be shown.

"""
print('********************* Data 1 ***************************')
T = Prims(G_one, 0, True, True)
print('********************* Data 2 ***************************')
T = Prims(G_two, 0, True, True)
print('********************* Data 3 ***************************')
T = Prims(G_three, 0, True, True)


