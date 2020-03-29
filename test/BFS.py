from _collections import deque
def BFS(G, node_s):
    node_s.cor = 'CINZA'
    node_s.distancia = 0
    node_s.predecessor = None
    G.append(node_s)
    while (len(G) != 0):
        u = G.popleft()
        for v in u.adj: #  o conjunto adj tem apenas strings ('A', 'B', ...); vai ter que arrumar isso ae pq v é pra ser os vértices
            if v.cor == 'BRANCO':
                v.cor = 'CINZA'
                v.distancia = u.distancia + 1
                v.predecessor = u
                G.append(v)
        u.cor = 'PRETO'

Q = deque()  #cria a fila Q
BFS(Q,nS)
for n in nodes:
    print('nó: {}\n'
          'cor: {}\n'
          'distancia: {}\n'
          'predecessor: {}\n'.format(n.nome,n.cor,n.distancia,n.predecessor))