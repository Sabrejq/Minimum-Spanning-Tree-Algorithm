<h1>Final Project Outline: MST Python Package </h1>
<p>
 Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together. A single graph can have many different spanning trees. A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with weight less than or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.</p>

<ol>
 
<h3>Prim’s algorithm </h3>
<li>Select any vertex </li>
<li>Select the shortest edge connected to that vertex</li>
<li>Select the shortest edge connected to any vertex already connected </li>
<li>Repeat step 3 until all vertices have been connected</li>

</ol>

-----
The project uses the following Python packages: 
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks [NetworkX](https://networkx.github.io/). `NetworkX`:

    networkx as nx
    
-----

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python [matplotlib](https://matplotlib.org/#). `matplotlib.pyplot`:

    matplotlib.pyplot as plt
    
    
-----

<h3> Usage </h3>
<hr>

```python
import networkx as nx
from algorithms.prims import Prims

G_one = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)
G_two = nx.read_weighted_edgelist('data/G2.txt', nodetype = int)
G_three = nx.read_weighted_edgelist('data/G3.txt', nodetype = int)


T = Prims(G_one, 0, True, True)

```
<p> You can change the values inside T to get the result you want. The argumets are G, the text file with the info, the starting node, True/False if you wasnt to display a graph, True/False if you want the graph info</p>

```python
def Prims(G, starting_node = 0, draw = False, attrib = False):
    T = nx.Graph();
    T.add_node(starting_node)
    
    if draw == True:
        draw_subtree(G, T)
        
    while set(T.nodes()) != set(G.nodes()):
        e = min_valid_edge(G, T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
        if draw == True:
            draw_subtree(G, T)
            
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
```
