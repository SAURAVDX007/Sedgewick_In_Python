from boiler_plate import *


class Bipartite:

    def __init__(self, graph):
        self.marked = [False for _ in range(graph.vertices)]
        self.color = [False for _ in range(graph.vertices)]
        self.is_bipartite = True

        for i in range(graph.vertices):
            if not self.marked[i]:
                self.dfs(graph, i)

    def dfs(self, graph, v):
        if self.marked[v]:
            return
        self.marked[v] = True
        neighbours = graph.adj(v)
        for neighbour in neighbours:
            if not self.marked[neighbour]:
                self.color[neighbour] = not self.color[v]
                self.dfs(graph, neighbour)
            else:
                if self.color[neighbour] == self.color[v]:
                    self.is_bipartite = False

    def is_graph_bipartite(self):
        return self.is_bipartite


# Code to test above implementation
bipartite = Bipartite(g)
print(bipartite.is_graph_bipartite())


