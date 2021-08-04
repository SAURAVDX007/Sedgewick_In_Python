from LinkedList import LinkedList


class Digraph:
    def __init__(self, vertices, edges=0):
        self.vertices = vertices
        self.edges = edges
        self.array = []

        for i in range(vertices):
            self.array.append(LinkedList())

    def add_edge(self, v, w):
        if v < self.vertices:
            self.array[v].insert_at_head(w)

    def print_graph(self):
        print("Directed Graph with", self.vertices, "vertices and", self.edges, 'edges')
        for i in range(self.vertices):
            print(i, end=" => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next_element
            print("None")

    def adj(self, source):
        if source >= self.vertices:
            raise IndexError("Source cannot be equal to or greater than the number of vertices")
        adjacent_list = []
        temp = self.array[source].get_head()
        while temp is not None:
            adjacent_list.append(temp.data)
            temp = temp.next_element
        return adjacent_list

    def reverse_of_digraph(self):
        digraph_reversed = Digraph(self.vertices, self.edges)
        for vertex in range(self.vertices):
            for w in self.adj(vertex):
                digraph_reversed.add_edge(w, vertex)
        return digraph_reversed
