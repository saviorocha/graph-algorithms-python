from _collections import defaultdict


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

nR = Node('r')
nS = Node('s')
nT = Node('t')
nU = Node('u')
nV = Node('v')
nW = Node('w')
nX = Node('x')
nY = Node('y')

nodes = (nR, nS, nT, nU, nV, nW, nX, nY)

edges = [(nR,nS), (nR,nV),
         (nS, nW),
         (nW,nT), (nW, nX),
         (nT, nU), (nT, nX),
         (nU, nY), (nU, nX),
         (nX, nY)]

graph = Graph(edges, nodes)
print(graph.__str__())