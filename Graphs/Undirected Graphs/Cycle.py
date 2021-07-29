from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edges(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)


class Cycle:
    def __init__(self, graph):
        self.marked = [False for _ in range(graph.vertices)]
        self.has_cycle = False
        for i in range(graph.vertices):
            if not self.marked[i]:
                self.dfs(graph, -1, i)

    def dfs(self, graph, u, v):
        if self.marked[v]:
            return
        self.marked[v] = True
        neighbours = graph.graph[v]
        for neighbour in neighbours:
            if not self.marked[neighbour]:
                self.dfs(graph, v, neighbour)
            elif neighbour != u:
                self.has_cycle = True

    def is_cyclic(self):
        return self.has_cycle


g = Graph(5)
g.add_edges(1, 0)
g.add_edges(1, 2)
g.add_edges(2, 0)
g.add_edges(0, 3)
g.add_edges(3, 4)

cycle = Cycle(g)
print(cycle.is_cyclic())

g1 = Graph(3)
g1.add_edges(0, 1)
g1.add_edges(1, 2)
cycle2 = Cycle(g1)
print(cycle2.is_cyclic())
