from LinkedList import LinkedList


# This graph can be made using
class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.array = []

        for i in range(vertices):
            self.array.append(LinkedList())

    def add_edges(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination)
            self.array[destination].insert_at_head(source)  # Undirected Graph

    def print_graph(self):
        print("Undirected Graph with", self.vertices, "vertices and", self.edges, 'edges')
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



