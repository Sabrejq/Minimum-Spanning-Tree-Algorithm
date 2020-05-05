# Function that sums the cost of the edges for a given Tree
def cost(G, e):
    return G.edges()[e]['weight']

# Function that counts the Edges aviable of a given Tree.
def incident_edges(G, T):
    # Creates empty list of edges
    edges = []  
    #Checks for edges in graph
    for e in G.edges():
        for v in T.nodes():
            if v in e:
                #Adds Edges to empty list 
                edges.append(e)
    return edges

# Function that counts the number of valid adges to use for a given Tree. 
def valid_edges(G, T): 
    #Temporary list of edges and incident edges
    edges=[]
    temp_edges = incident_edges(G, T)
    for e in temp_edges:
        # Checks for next edge and appends it if not found
        if e[0] not in T.nodes() or e[1] not in T.nodes():
            edges.append(e)
    return edges

# Function that returns the minimum number of edges to traverse a Tree once.
def min_valid_edge(G, T):
    edges = valid_edges(G, T)
    min_edge = edges[0]
    #Checks for the cost to of edges and selects the most optimal to add to the list
    for e in edges:
        if cost(G, e) < cost(G, min_edge):
            min_edge = e
    return min_edge  


