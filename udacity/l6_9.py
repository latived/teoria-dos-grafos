# Comentários por mim (25/03)

##################################################################
# Traversal...
# Call this routine on nodes being visited for the first time
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            # Vai fazendo um busca em profundidade, marcando cada um dos
            # vértices vizinhos ao 'node'
            total_marked += mark_component(G, neighbor, marked)
    return total_marked # total de vértices no componente

def check_connection(G, v1, v2):
    # Return True if v1 is connected to v2 in G
    # or False if otherwise

    # Podemos ir de v1 a v2 apenas se no componente começando de v1 há um caminho
    # para v2
    marked = {}
    mark_component(G, v1, marked)
    if v2 not in marked.keys():
        return False
    return True
    
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'), 
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
    G = {}
    for v1, v2 in edges:
        make_link(G, v1, v2)
    assert check_connection(G, "a", "c") == True
    assert check_connection(G, 'a', 'b') == False
    



