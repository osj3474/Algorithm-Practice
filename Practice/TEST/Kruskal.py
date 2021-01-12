class DisjointSet :
    def __init__(self, n) :
        self.parent = {}
        self.rank = {}
        for i in range(n) :
            self.parent[i] = i
            self.rank[i] = 0

    def Find(self, v) :
        if self.parent[v] != v :
            self.parent[v] = self.Find(self.parent[v])
        return self.parent[v]

    def Union(self, root1, root2) :
        if self.rank[root1] > self.rank[root2] :
            self.parent[root2] = root1
        else :
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2] :
                self.rank[root2] += 1


def kruskal(n, info) :
    minimum_weight = 0
    disjointset = DisjointSet(n)
    result = []
    for data in sorted(info, key = lambda cost: cost[2]) :
        v, u, weight = data
        root1 = disjointset.Find(v)
        root2 = disjointset.Find(u)
        if root1 != root2 :
            disjointset.Union(root1, root2)
            result.append(data)
            minimum_weight += data[2]
    return result, minimum_weight

result = 0
minimum_weight = 0
result, minimum_weight = kruskal(6, [[0,1,5], [0,3,2], [0,4,3], [1,4,1], [3,4,10],[1,2,2],[2,5,3],[4,5,4]])
print(result, minimum_weight)
