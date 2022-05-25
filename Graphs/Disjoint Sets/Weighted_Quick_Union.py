class WeightedQuickUnion:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.sz = [1 for i in range(size)]  # this stores the number of node in tree at a point

    def find(self, p):
        while p != self.root[p]:
            p = self.root[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i != j:
            if self.sz[i] < self.sz[j]:
                self.root[i] = j
                self.sz[j] += self.sz[i]
            else:
                self.root[j] = i
                self.sz[i] += self.sz[j]


# Test Case
uf = WeightedQuickUnion(10)
uf.union(4, 3)
uf.union(3, 8)
uf.union(6, 5)
uf.union(9, 4)
uf.union(2, 1)
uf.union(8, 9)
uf.union(5, 0)
uf.union(7, 2)
uf.union(6, 1)
uf.union(1, 0)
uf.union(6, 7)
print(uf.connected(1, 5))
print(uf.connected(5, 7))
print(uf.connected(4, 9))
print(uf.connected(4, 5))
# print(uf.sz)

