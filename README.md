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
----------------------------------------------------------------------------------------------------------------------
The project uses the following Python packages: 
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. `NetworkX`:

    networkx as nx
    
----------------------------------------------------------------------------------------------------------------------
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. `matplotlib.pyplot`:

    matplotlib.pyplot as plt
    
    ----------------------------------------------------------------------------------------------------------------------
