# from Graph import Graph

# Construct Graph
# input_file = open('/Users/sauravkumar/PycharmProjects/data/tinyCG.txt', 'r')
# number_of_vertices = int(input_file.readline().strip('\n'))
# number_of_edges = int(input_file.readline().strip('\n'))
# g = Graph(number_of_vertices, number_of_edges)
# for line in input_file:
#     edge1 = int(line.strip('\n').split(" ")[0])
#     edge2 = int(line.strip('\n').split(" ")[1])
#     g.add_edges(edge1, edge2)

# g.print_graph()


# marked = [False for i in range(number_of_vertices)]
# print(marked)


# def depth_first_search(graph, source):
#     if marked[source]:
#         return
#     marked[source] = True
#     neighbours = graph.adj(source)
#     for neighbour in neighbours:
#         depth_first_search(graph, neighbour)
#
#
# depth_first_search(g, 0)
# print(marked)

# But the above code does not take into account the various different connected components
# input_file = open('/Users/sauravkumar/PycharmProjects/data/tinyG.txt', 'r')
# number_of_vertices = int(input_file.readline().strip('\n'))
# number_of_edges = int(input_file.readline().strip('\n'))
# g = Graph(number_of_vertices, number_of_edges)
# for line in input_file:
#     edge1 = int(line.strip('\n').split(" ")[0])
#     edge2 = int(line.strip('\n').split(" ")[1])
#     g.add_edges(edge1, edge2)
#
#
# marked = [False for i in range(number_of_vertices)]
# print(marked)

from boiler_plate import *


def depth_first_search(graph, source):
    if marked[source]:
        return
    marked[source] = True
    print("The current vertex is ", source, end='  ')
    neighbours = graph.adj(source)
    for neighbour in neighbours:
        depth_first_search(graph, neighbour)


# depth_first_search(g, 0)
# print(marked)

for i in range(number_of_vertices):
    if not marked[i]:
        depth_first_search(g, i)
        print()

print(marked)
