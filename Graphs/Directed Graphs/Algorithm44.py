from boiler_plate import *


class DirectedDFS:

    # def __init__(self, graph, source):
    #     self.marked = [False for _ in range(graph.vertices)]
    #     self.dfs(graph, source)

    # This is for multiple source reachability
    def __init__(self, graph, sources):
        self.marked = [False for _ in range(graph.vertices)]
        for source in sources:
            if not self.marked[source]:
                self.dfs(graph, source)

    def dfs(self, graph, source):
        if self.marked[source]:
            return
        self.marked[source] = True
        neighbours = graph.adj(source)
        for neighbour in neighbours:
            if not self.marked[neighbour]:
                self.dfs(graph, neighbour)

    def marked(self, v):
        return self.marked[v]


# Code to test above implementation from 1st constructor. Uncomment 1st constructor, and comment 2nd one
# digraph = DirectedDFS(g, 0)
# digraph = DirectedDFS(g, 1)
# print(digraph.marked)

# Code to test multi source reachability. Comment 1st constructor, and uncomment 2nd constructor.
digraph = DirectedDFS(g, [0, 6])
print(digraph.marked)

