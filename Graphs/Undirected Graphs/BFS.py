from boiler_plate import *
from Queue import MyQueue
queue = MyQueue()


def Breadth_First_Search(graph, source):
    marked[source] = True
    queue.enqueue(source)

    while not queue.is_empty():
        current_vertex = queue.dequeue()
        neighbours = graph.adj(current_vertex)
        for neighbour in neighbours:
            if not marked[neighbour]:
                marked[neighbour] = True
                queue.enqueue(neighbour)


Breadth_First_Search(g, 0)
print(marked)

# Similarly we can iterate over a list of vertices to cover for all the different connected components
