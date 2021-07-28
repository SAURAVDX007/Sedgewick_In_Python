from boiler_plate import *
from Stack import MyStack


class DepthFirstPaths:
    def __init__(self, graph, source_vertex):
        self.source = source_vertex
        self.marked = [False for _ in range(graph.vertices)]
        self.edge_to = [0 for _ in range(graph.vertices)]
        self.dfs(graph, self.source)

    def dfs(self, graph, vertex):
        if self.marked[vertex]:
            return
        self.marked[vertex] = True
        neighbours = graph.adj(vertex)
        for neighbour in neighbours:
            if not self.marked[neighbour]:
                self.edge_to[neighbour] = vertex
                self.dfs(graph, neighbour)

    def has_path_to(self, target_vertex):
        return self.marked[target_vertex]

    def path_to(self, target_vertex):
        if not self.marked[target_vertex]:
            return "No Path exists between", self.source, "and", target_vertex
        stack_for_path = MyStack()
        x = target_vertex
        while x != self.source:
            stack_for_path.push(x)
            x = self.edge_to[x]
        stack_for_path.push(self.source)
        return stack_for_path.stack_list


# Testing above code functionality on tinyCG.txt file
depth_first_path = DepthFirstPaths(g, 0)
print(depth_first_path.marked)


# client code to get path from source to target using path_to method from above class
for v in range(g.vertices):
    print(depth_first_path.source, "to", v, ": ", end="")
    if depth_first_path.has_path_to(v):
        for i in reversed(depth_first_path.path_to(v)):
            if i == depth_first_path.source:
                print(i, end="")
            else:
                print("-", i, end="")
        print()






