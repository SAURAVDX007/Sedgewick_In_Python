class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        findX = self.find(x)
        findY = self.find(y)
        if findX != findY:
            for i in range(len(self.root)):
                if self.root[i] == findY:
                    self.root[i] = findX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(10)
uf.union(0, 1)
uf.union(1, 3)
uf.union(0, 2)
uf.union(4, 8)
uf.union(5, 6)
uf.union(6, 7)
print(uf.connected(0, 3))
print(uf.connected(4, 9))
print(uf.connected(5, 7))
print(uf.connected(3, 6))

