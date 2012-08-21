
# Deep search algorithm to find an Hamiltonian path in a graph
# (visiting every edge once and only once)
"""
EXAMPLES

V = [1,2,3,4,5,6]
E = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1),(2,6),(6,4),(4,2)]
returns [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 1], [3, 4, 5, 6, 1, 2],
         [4, 5, 6, 1, 2, 3], [5, 6, 1, 2, 3, 4], [6, 1, 2, 3, 4, 5]]

V = [1,2,3,4]
E = [(1,2),(1,4),(2,3),(3,4),(2,4)]
returns [[1, 2, 3, 4]]


V = ['AA','AB','BC','CD','DE','EF']
E = [('AA','AB'),('AB','BC'),('BC','CD'),('CD','DE'),('DE','EF'),('EF','AA'),('AB','EF'),('EF','CD'),('CD','AB')]
returns [['AA','AB','BC','CD','DE','EF'], ['AB','BC','CD','DE','EF','AA'], ['BC','CD','DE','EF','AA','AB'],
         ['CD','DE','EF','AA','AB','BC'], ['DE','EF','AA','AB','BC','CD'], ['EF','AA','AB','BC','CD','DE']]
"""

class Node(object):
    def __init__(self, name='',idx=-1,active=1,label=''):
        self.name = name        # node name
        self.idx = idx          # node index
        self.active = active    # activity flag
        self.label = label      # current state
        self.inc_edges = set()  # incoming edges
        self.out_edges = set()  # outgoing edges
        self.edges = set()      # all communicating edges
        self.neighbours = set() # all accessible nodes

    def __eq__(self,node):
        return self.idx == node.idx and self.name == node.name

class Vertex(object):
    def __init__(self,inc,out, name='',label='',active=1):
        assert isinstance(inc,Node), "Expected Node class, got %s." % type(inc)
        assert isinstance(out,Node), "Expected Node class, got %s." % type(out)
        self.inc = inc          # node it comes from
        self.out = out          # node it goes to
        self.name = ''          # vertex name
        self.active = 1         # activity flag
        self.label = ''         # current state

    def __getitem__(self,i):
        if i==0: return self.inc
        if i==1: return self.out


def hamiltonian(V, E):
    E = set([Vertex(Node(name=e[0],idx=V.index(e[0])),Node(name=e[1],idx=V.index(e[1]))) for e in E])
    V = [Node(idx=i,name=V[i]) for i in range(len(V))]
    for e in E:
        V[e[0].idx].neighbours.add(V[e[1].idx])

    L = 1
    paths = [[v] for v in V]
    while L < len(V):
        q = []
        toremove = []
        for p in paths:
            if p[-1].neighbours:
                for n in p[-1].neighbours:
                    if n not in p:
                        q.append(p+[n])
            else:
                toremove.append(p)
        for p in toremove: paths.remove(p)
        L+=1
        paths = q

    return [[n.name for n in p] for p in paths]

