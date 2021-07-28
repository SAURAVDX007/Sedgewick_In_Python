from boiler_plate import *
from Queue import MyQueue
from Stack import MyStack


class BreadthFirstPaths:
    def __init__(self, graph, source):
        self.source = source
        self.marked = [False for _ in range(graph.vertices)]
        self.edge_to = [0 for _ in range(graph.vertices)]
        self.BFS(graph, self.source)

    def BFS(self, graph, source):
        queue = MyQueue()
        queue.enqueue(source)
        self.marked[source] = True

        while not queue.is_empty():
            current_vertex = queue.dequeue()
            neighbours = graph.adj(current_vertex)
            for neighbour in neighbours:
                if not self.marked[neighbour]:
                    self.edge_to[neighbour] = current_vertex
                    self.marked[neighbour] = True
                    queue.enqueue(neighbour)

    def has_path_to(self, vertex):
        return self.marked[vertex]

    def path_to(self, vertex):
        if not self.has_path_to(vertex):
            return "Path from", self.source, "to", vertex, "doesn't exist"
        stack = MyStack()
        x = vertex
        while x != self.source:
            stack.push(x)
            x = self.edge_to[x]
        stack.push(self.source)
        return stack.stack_list


# code to test above implementation.
breadth_first_paths = BreadthFirstPaths(g, 0)
for v in range(g.vertices):
    print(breadth_first_paths.source, "to", v, ": ", end="")
    for i in breadth_first_paths.path_to(v)[::-1]:
        if i == breadth_first_paths.source:
            print(breadth_first_paths.source, end="")
        else:
            print("-", i, end="")
    print()


