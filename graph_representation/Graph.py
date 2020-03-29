from _collections import defaultdict
from _collections import deque
import heapq

class Node:
    def __init__(self, nome):
        self.nome = nome
        # if (not origem):
        self.cor = 'BRANCO'
        self.predecessor = None
        self.distancia = None
        self.adj = None

class Graph:
    """
    Graph data structure, undirected by default.
    defaultdict: Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in
    the dictionary. The defaultdict in contrast will simply create any items that you try to access (provided of course they do
    not exist yet). To create such a "default" item, it calls the function object that you pass to the constructor (more
    precisely, it's an arbitrary "callable" object, which includes function and type objects). For the first example, default
    items are created using int(), which will return the integer object 0. For the second example, default items are created
    using list(), which returns a new empty list object.
    """

    def __init__(self, edges, nodes, directed=False):
        self.__graph = defaultdict(set)  # dicionario default com a classe Set no construtor; usa-se a classe set para que um vértice(chave) aponte para mais de um vértice
        self.__nodes = nodes
        self.__directed = directed
        self.add_connections(edges)
        self.addLista(nodes, self.__graph)

    def add_connections(self, edges):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in edges:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self.__graph[node1].add(node2)
        if not self.__directed:
            self.__graph[node2].add(node1)

    def addLista(self, nodes, graph):
        for i in range(len(nodes)):
            nodes[i].adj = graph[nodes[i]]
        # for n in nodes:
        #     for k in graph:
        #         n.adj[k] = graph[k]

    def remove(self, node):  # erro RuntimeError: dictionary changed size during iteration
        """ Remove all references to node """

        for n, cxns in self.__graph.items():  # para iterar um dicionario com default usa-se xxxxx.items()
            try:
                cxns.remove(node)  # remove-se todos os elementos do set(as arestas)
            except KeyError:
                pass
            try:
                del self.__graph[node]  # remove-se o item do dicionario(vértice)
            except KeyError:
                pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self.__graph and node2 in self.__graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self.__graph:
            return None
        for node in self.__graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.__graph))

# n1 = Node('1')
# n2 = Node('2')
# n3 = Node('3')
# n4 = Node('4')
# n5 = Node('5')
# n6 = Node('6')
#
# edges = [(n1, n2), (n2, n3), (n2, n4), (n3, n4), (n5, n6), (n6, n3)]
# nodes = (n1, n2, n3, n4, n5, n6)


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

# V: lista de vertices
# Q: Fila de prioridade mínima de vértices
# S: Conjuntos de vértices cujos pesos finais de caminhos mais curtos de s até a origem já foram determinados
def Dijkstra(V, Q, S, node_s):
    initialize_single_source(V, node_s)
    Q = V
    while(Q != None):
        u = heapq.heappop(q)
        S = S | u
        for v in u.adj:
            relax(u, v, w)

def initialize_single_source(V, node_s):
    for v in V:
        v.distancia = None
        v.predecessor = None
        node_s.distancia = 0

def relax(u, v, w):
    pass

nR = Node('r')
nS = Node('s')
nT = Node('t')
nU = Node('u')
nV = Node('v')
nW = Node('w')
nX = Node('x')
nY = Node('y')

nodes = (nR, nS, nT, nU, nV, nW, nX, nY)
nodesQ = []  # criar uma lista de prioridades dos vértices para o Dijkstra

edges = [(nR, nS), (nR, nV),
        (nS, nW),
        (nW, nT), (nW, nX),
        (nT, nU), (nT, nX),
        (nU, nY), (nU, nX),
        (nX, nY)]

weight = {
    edges[0]
}
for i in range(10):
    for n1, n2 in edges:
        key = (n1.nome, n2.nome)
        weight['-'.join(key)] = i

graph = Graph(edges, nodes)
print(graph.__str__())

Q = deque()
BFS(Q, nS)

q = []
S = set()

for n in nodes:
    print('nó: {}\n'
          'cor: {}\n'
          'distancia: {}\n'
          'predecessor: {}\n'.format(n.nome,n.cor,n.distancia,n.predecessor))
# print(graph.__str__())
# for n in nodes:
#     print('nó {}: {}'.format(n.nome, n.adj))