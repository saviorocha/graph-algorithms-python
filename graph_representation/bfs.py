from _collections import deque
from  .Graph import Graph, Node

def BFS(G, node_s):
    node_s.cor = 'CINZA'
    node_s.distancia = 0
    node_s.predecessor = None
    G.append(node_s)
    while (len(G) != 0):
        u = G.popleft()
        for v in u.adj[u.nome]:
            if v.cor == 'BRANCO':
                v.cor = 'CINZA'
                v.distancia = u.distancia + 1
                v.predecessor = u
                G.append(v)
        u.cor = 'PRETO'
n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')

edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
nodes = (n1, n2, n3, n4, n5, n6)
graph = Graph(edges, nodes)
Q = deque()
BFS(Q,n1)