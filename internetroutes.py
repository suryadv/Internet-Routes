from collections import deque, namedtuple

inf = float('inf')                                    #initialize default distance to nodes as infinity
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )


    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def shortestpath(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = sorted(self.vertices.copy())

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path

    def add_edge(self, n1, n2, cost=1, both_ends=True):              #used to add edges manually in code along with cost
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    def p2p(edgeslist):
        peern = []
        for check in edgeslist:
            if (check[::-1]) in edgeslist:
                peern.append(check)
        return peern

    def listnodes(contents):
        node = []
        nodes = []
        for item in contents:
            for items in item:
                node.append(items)
        nodes = (sorted(set(node)))            #sorting set , contains all i/p nodes
        return nodes

    def pathoutput(target,NodesList):
        lex = []
        for elem in NodesList:
            path = graph.shortestpath(target,elem)
            op = ','.join(path)
            lex.append(op)
        return lex


#reading edge input list
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(tuple(line.split(",")))

z1 = contents                                            #contains list of all one peering relationship i/p
peerN = Graph.p2p(z1)                                    # eliminates non peer nodes
graph = Graph(peerN)                                     # creates graph with peer nodes
NodesList = Graph.listnodes(peerN)                       #creates a nodes list of all nodes present in edge list
routes = Graph.pathoutput('INTERNET',NodesList)          #creates shortest path from all nodes to source
for final in sorted(routes):
    print(final)                                          #prints shortest path lexicographically

