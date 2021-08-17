from boiler_plate import *
from Stack import MyStack


class DirectedCycle:

    def __init__(self, digraph):
        self.marked = [False for _ in range(digraph.vertices)]
        self.edge_to = [0 for _ in range(digraph.vertices)]
        self.on_stack = [False for _ in range(digraph.vertices)]
        self.cycle = MyStack()
        for v in range(digraph.vertices):
            if not self.marked[v]:
                self.dfs(digraph, v)

    def dfs(self, digraph, v):
        self.marked[v] = True
        self.on_stack[v] = True
        neighbours = digraph.adj(v)
        for neighbour in neighbours:
            if self.has_cycle():
                return
            elif not self.marked[neighbour]:
                self.edge_to[neighbour] = v
                self.dfs(digraph, neighbour)
            elif self.on_stack[neighbour]:

                x = v
                while x != neighbour:
                    self.cycle.push(x)
                    x = self.edge_to[x]
                self.cycle.push(neighbour)
                self.cycle.push(v)
        self.on_stack[v] = False

    def has_cycle(self):
        return self.cycle.stack_size != 0

    def cycle(self):
        return self.cycle


# Test code for above implementation
# cycle_detection = DirectedCycle(g)
# print(cycle_detection.has_cycle())
#
# cycle_stack = cycle_detection.cycle.stack_list
# for vertex in reversed(cycle_stack):
#     print(vertex)



