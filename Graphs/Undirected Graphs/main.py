# First we would like to read from Sedgewick provided file and then print our graph

from Graph import Graph

# Get number of vertices and edges from data files
# input_file = open('/Users/sauravkumar/PycharmProjects/data/tinyG.txt', 'r')
input_file = open('/Users/sauravkumar/PycharmProjects/data/mediumG.txt', 'r')
number_of_vertices = int(input_file.readline().strip('\n'))
number_of_edges = int(input_file.readline().strip('\n'))
# print(number_of_vertices)
# print(number_of_edges)

g = Graph(number_of_vertices, number_of_edges)
for line in input_file:
    edge1 = int(line.strip('\n').split(" ")[0])
    edge2 = int(line.strip('\n').split(" ")[1])
    g.add_edges(edge1, edge2)

g.print_graph()
# We can also get adjacent neighbours of any vertex
# print(g.adj(10))


# Typical Graph Processing codes
# Compute the degree of a vertex:

def degree_of_a_vertex(source):
    adjacent_vertex_list = g.adj(source)
    return len(adjacent_vertex_list)


# print(degree_of_a_vertex(2))

# Compute the maximum degree of all vertex and return that vertex as a pair containing vertex and its degree
def maximum_degree(graph):
    num_of_vertices = graph.vertices
    max_degree = 0
    for i in range(num_of_vertices):
        current_degree = degree_of_a_vertex(i)
        if current_degree > max_degree:
            max_degree = current_degree
            answer = [i, max_degree]
    return answer


# print(maximum_degree(g))


# Compute the average degree
def average_degree(graph):
    num_of_vertices = graph.vertices
    sum_of_degrees = 0
    for i in range(num_of_vertices):
        current_degree = degree_of_a_vertex(i)
        sum_of_degrees += current_degree
    return sum_of_degrees / graph.vertices


# print(average_degree(g))


# Sedgewick average degree computation
def average_degree2(graph):
    return 2 * graph.edges / graph.vertices
# Why 2? Because if you check the input file, it states "0 2" for an edge between 0 to 2, but doesn't mention "2 0"


# print(average_degree2(g))


# Count number of self loops
def count_num_of_self_loops(graph):
    num_of_vertices = graph.vertices
    count = 0
    for i in range(num_of_vertices):
        adjacent_vertex = graph.adj(i)
        for j in adjacent_vertex:
            if i == j:
                count += 1
    return count // 2         # Each edge gets counted twice


# print(count_num_of_self_loops(g))



