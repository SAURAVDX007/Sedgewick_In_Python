from boiler_plate import *


class ConnectedComponents:

    def __init__(self, graph):
        self.marked = [False for _ in range(graph.vertices)]
        self.count = 0
        self.id = [0 for _ in range(graph.vertices)]
        for vertex in range(graph.vertices):
            if not self.marked[vertex]:
                self.count += 1
                self.dfs(graph, vertex, self.count)

    def dfs(self, graph, source, count):
        if self.marked[source]:
            return
        self.marked[source] = True
        self.id[source] = count
        neighbours = graph.adj(source)
        for neighbour in neighbours:
            if not self.marked[neighbour]:
                self.dfs(graph, neighbour, count)

    def connected(self, vertex1, vertex2):
        return self.id[vertex1] == self.id[vertex2]

    def id_of_vertex(self, vertex):
        return self.id[vertex]

    def count_of_components(self):
        return self.count


# Code to test above implementation based on tinyG.txt file.
cc = ConnectedComponents(g)
print(cc.id)
print(cc.connected(1, 9))
print(cc.connected(1, 3))
print(cc.connected(7, 8))
print(cc.connected(7, 12))
print(cc.count_of_components())
print(cc.id_of_vertex(7))

