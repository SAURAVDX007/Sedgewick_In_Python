from DepthFirstOrder import DepthFirstOrder
from boiler_plate import *


class KosharajuSharirScc:

    def __init__(self, digraph):
        self.marked = [False for _ in range(digraph.vertices)]
        self.id_of_vertex = [-1 for _ in range(digraph.vertices)]
        self.count = 0
        reverse_graph = Digraph.reverse_of_digraph(digraph)
        order = DepthFirstOrder(reverse_graph)
        rev_post = order.reverse_postorder().stack_list
        for vertex in reversed(rev_post):
            if not self.marked[vertex]:
                self.DFS(digraph, vertex)
                self.count += 1

    def DFS(self, digraph, ver):
        if self.marked[ver]:
            return
        self.marked[ver] = True
        self.id_of_vertex[ver] = self.count
        neighbours = digraph.adj(ver)
        for neighbour in neighbours:
            if not self.marked[neighbour]:
                self.DFS(digraph, neighbour)

    def strongly_connected(self, v, w):
        return self.id_of_vertex[v] == self.id_of_vertex[w]

    def id_component(self, v):
        return self.id_of_vertex[v]

    def count_of_strong_components(self):
        return self.count


# Code to test above implementation
strong_components = KosharajuSharirScc(g)
print(strong_components.id_of_vertex)
