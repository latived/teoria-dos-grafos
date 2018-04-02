#!/usr/bin/env python3

# Ele usa um vetor chamado anterior, para da conta da última linha das tabelas
# que construímos. O conjunto A (Aberto) contém todos os vértices no início e o
# F (Fechado) é vazio.

def intersect(A, B):
    # extremamente feio e ineficiente
    # um for seria melhor?
    return list(set.intersection(set(A), set(B)))

def dijkstra(G, v):
    # Vetor de distâncias a partir de v0
    ds = [10e10 for _ in range(len(G))] 
    ds[0] = 0    # ds[0] = 0, dist de v0 para ele mesmo é 0
    A = list(G.keys())
    F = []
    anterior = [0 for _ in range(len(G))]
    while (len(A) != 0):
        vr = 10e10
        for arestas in G[v]:
            if (arestas[1] < vr):
                r = arestas[0]     # vértice mais próximo
                vr = arestas[1]    # valor até o vértice mais pŕoximo
        F.append(r)
        A.remove(r)
        S = intersect(A, [s[0] for s in G[r]])
        for i in S:
            for aresta in G[r]:
                if i == arestas[0]:
                    ri = arestas[1]
                    p = min(ds[i], vr + ri)
                    if p < ds[i]:
                        ds[i] = p
                        anterior[i] = r

    print(ds)
    print(anterior)

def main():
    # ...
    G = {0: [(1,12), (2,4)],
         1: [(2,6), (3,6)],
         2: [(1,10), (3,2), (4,2)],
         3: [(2,8), (5,6)],
         4: [(1,2), (5,6)],
         5: []
        }
    dijkstra(G, 0)

if __name__ == "__main__":
    main()
