#!/usr/bin/env python3

# Algoritmo de Malgrange
#
#   Este algoritmo constrói os dois fechos transitivos de um vértice,
#   faz a intersecção deles e retira do grafo os vértices dessa intersecção,
#   antes de tomar um novo vértice etc., etc., até que todos os vértices
#   estejam separados em suas componenetes.
#
#   Isto é feito iterativamente, varrendo-se a matriz (ou a lista) de
#   adjacência à procura das vizinhanças dos vértices encontrados, até que não
#   apareçam novos vértices a serem incluídos.

# O fecho transitivo direto procura (iterativamente) sucessores de vértices e é
# o conjunto de todos os vértices atingíveis a partir de v. Estes vértices são
# chamados de descendentes de v.
# RECEBE: 
#   G é o grafo
#   Rp armazena os descentendes do vértice
def ft_direto(G, Rp):
    sucessores = []
    for v in Rp:
        for s in G[v]: 
            if s not in Rp:
                sucessores.append(s)
    return sucessores

# O fecho transitivo inverso procura (iterativamente) antecessores de vértices e é
# o conjunto de todos os vértices a partir dos quais v é atingível. Estes vértices são
# chamados de ascendentes de v.
# RECEBE:
#   G é o grafo
#   Rm armazena os ascendentes do vértice
def ft_inv(G, Rm):
    antecessores = []
    for v in Rm:
        for k in G.keys():
            if v in G[k] and k not in Rm:
                antecessores.append(k)
    return antecessores

# Retorna intersecção de listas
# Certamente há formas mais eficientes
def intersec(Rp, Rm):
    return set.intersection(set(Rp), set(Rm))

# G é uma lista de adjacências
def malgrange(G):
    Y = set(G.keys())  # Armazena os vértices ainda não pertecentens a uma componente
    I = 0   # Indexa as componentes conexas encontradas
    componentes = []
    while len(Y): # enquanto Y não for vazio
        Rp = []     # R+ armazena os descendentes do vértice em questão
        Rm = []     # R- armazena os ascendentes do vértice em questão
        v = Y.copy().pop()     # Copio para não modificar o Y original 
        W = []
        Rp.append(v)
        # Provavelmente não preciso somar,
        # pois ft_direto toda vez constrói a lista de sucessores
        while (W != Rp + ft_direto(G, Rp)):
            Rp.extend(ft_direto(G, Rp))
            W = Rp.copy()

        W = [] 
        Rm.append(v)
        # Mesma coisa aqui em relação a soma
        while (W != Rm + ft_inv(G, Rm)):
            Rm.extend(ft_inv(G, Rm))
            W = Rm.copy()

        componentes.append(intersec(Rp, Rm))
        Y = Y - componentes[I]
        I += 1
    return componentes

def main():
    G = {
       1: [4],
       2: [1, 5, 6],
       3: [2, 4],
       4: [5],
       5: [4],
       6: [3, 5]}    

    print(malgrange(G))

if __name__ == "__main__":
    main()
