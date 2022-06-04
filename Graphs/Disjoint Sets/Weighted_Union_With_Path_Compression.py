class WeightedQuickUnionPathCompression:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.sz = [1 for i in range(size)]  # this stores the number of node in tree at a point

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

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
uf = WeightedQuickUnionPathCompression(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
