from functions.prims_functions import cost, min_valid_edge
from functions.drawings import draw_subtree
import networkx as nx

def Prims(G, starting_node = 0, draw = False, attrib = False):
    
    # Empty graph is created 
    T = nx.Graph();
    
    #Attribute 2, starting node
    T.add_node(starting_node)
    
    #Attribute 3, if True graph will be drawn
    if draw == True:
        draw_subtree(G, T)
        
    """
    Uses min_valid_edge function to draw the a sub tree and to show a graph
    with the minimun valid edges to traverse the tree. 
    """
    while set(T.nodes()) != set(G.nodes()):
        e = min_valid_edge(G, T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
        if draw == True:
            draw_subtree(G, T)
            
    #Attribute 4, if true info bellow will be shown 
    if attrib == True:
        total_cost = sum(cost(G, e) for e in T.edges())
        print('')
        print('-------------- Properties of the Tree T --------------')
        print('-----------------------------------------------------')
        print(f'V(T) = {list(T.nodes())} ')
        print(f'E(T) = {list(T.edges())} ')
        print(f'Total Cost = {total_cost}')
        print('-----------------------------------------------------')
        
    return T
