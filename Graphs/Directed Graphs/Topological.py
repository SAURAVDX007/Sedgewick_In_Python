from DepthFirstOrder import DepthFirstOrder
from DirectedCycle import DirectedCycle
from boiler_plate import *


class Topological:
    def __init__(self, digraph):
        self.cycle_finder = DirectedCycle(digraph)
        if not self.cycle_finder.has_cycle():
            self.dfs = DepthFirstOrder(digraph)
            self.order = self.dfs.reverse_postorder()

    def topological_sort_order(self):
        return self.order

    def has_order(self):
        return self.order is not None


# Code to test above implementation -> file used tinyDAG.txt
topological = Topological(g)
print(topological.has_order())
order = topological.topological_sort_order().stack_list
for v in reversed(order):
    print(v)


