from Graph import Graph


class SymbolGraph:

    def __init__(self, filename, delimiter):
        self.st = dict()  # Key-> String, Value-> Integer
        self.keys = []

        input_file = open(filename)
        for line in input_file:
            adjacent = line.strip().split(delimiter)
            for i in adjacent:
                if i not in self.st:
                    self.st[i] = len(self.st)
        for key in self.st.keys():
            self.keys.append(key)

        # Here we create our graph instance. this needed little modification to original graph class
        # where we had to change the edges to default to 0 if not provided in graph constructor.
        self.graph = Graph(len(self.st))
        input_file.close()
        input_file = open(filename)
        for line in input_file:
            adjacent = line.strip().split(delimiter)
            vertex = self.st[adjacent[0]]
            for i in adjacent[1:]:
                self.graph.add_edges(vertex, self.st[i])
        input_file.close()

    def contains(self, s):
        return s in self.st

    def index_of(self, s):
        return self.st[s]

    def name_of(self, v):
        return self.keys[v]

    def graph(self):
        return self.graph


# Test codes
# symbol = SymbolGraph('/Users/sauravkumar/PycharmProjects/data/routes.txt', " ")
# # print(symbol.st)
#
# # Get adjacent vertices to a vertex
# source = 'JFK'
# for v in symbol.graph.adj(symbol.index_of(source)):
#     print(symbol.name_of(v))

symbol2 = SymbolGraph('/Users/sauravkumar/PycharmProjects/data/movies.txt', "/")
print(symbol2.st)

# Get adjacent vertices to a vertex
source = 'Bacon, Kevin'
for v in symbol2.graph.adj(symbol2.index_of(source)):
    print(symbol2.name_of(v))

print("++++++++++++++++++++")
source = 'Titanic (1997)'
for v in symbol2.graph.adj(symbol2.index_of(source)):
    print(symbol2.name_of(v))
