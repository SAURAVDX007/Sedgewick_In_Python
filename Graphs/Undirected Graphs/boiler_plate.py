from Graph import Graph
# Note that the files keep on changing with algorithms.
input_file = open('/Users/sauravkumar/PycharmProjects/Sedgewick_Python/Graphs/Undirected Graphs/bipartite.txt', 'r')
number_of_vertices = int(input_file.readline().strip('\n'))
number_of_edges = int(input_file.readline().strip('\n'))
g = Graph(number_of_vertices, number_of_edges)
for line in input_file:
    edge1 = int(line.strip('\n').split(" ")[0])
    edge2 = int(line.strip('\n').split(" ")[1])
    g.add_edges(edge1, edge2)


marked = [False for i in range(number_of_vertices)]
# print(marked)
