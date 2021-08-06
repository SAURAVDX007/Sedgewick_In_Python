from Digraph import Digraph
# Note that the files keep on changing with algorithms.
input_file = open('/Users/sauravkumar/PycharmProjects/data/tinyDG.txt', 'r')
# Changed the spacing in tinyDG.txt file (removed unwanted spaces)
number_of_vertices = int(input_file.readline().strip('\n'))
number_of_edges = int(input_file.readline().strip('\n'))
g = Digraph(number_of_vertices, number_of_edges)
for line in input_file:
    edge1 = int(line.strip('\n').split(" ")[0])
    edge2 = int(line.strip('\n').split(" ")[1])
    g.add_edge(edge1, edge2)

# marked = [False for i in range(number_of_vertices)]
# print(marked)
# g.print_graph()
# digraph_reverse = g.reverse_of_digraph()
# print("*"*50)
# digraph_reverse.print_graph()
