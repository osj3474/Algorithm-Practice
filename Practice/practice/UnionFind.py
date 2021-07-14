# 반례
def Find(v, parent) :
    if parent[v] != v :
        parent[v] = Find(parent[v], parent)
    return parent[v]

def Union(x, y, parent, rank) :
    # if x ==1 and y == 0:
    #     print(parent)
    #     print(rank)
    if rank[x] > rank[y] :
        parent[y] = x
    elif rank[x] < rank[y] :
        parent[x] = y
    else :
        parent[y] = x
        rank[x] += 1
    return parent, rank

def solution(n, computers):
    parent = {}
    rank = {}
    # Make set
    for i in range(n) :
        parent[i] = i
        rank[i] = 0
    ## computers[i].index(edge) ---- 고유 인덱스가 저장이 되지 않는다!!!
    for i in range(len(computers)) :
        for edge in range(len(computers[i])) :
            if computers[i][edge] == 1 and edge != i :
                v1 = i
                v2 = edge
                # print("원본:", v1, v2)
                x = Find(v1, parent)
                y = Find(v2, parent)
                if x != y :
                    parent, rank = Union(x, y, parent, rank)
    # for i in range(n) :
    #     root = Find(i, parent)
    #     parent[i] = root
    value = list(parent.values())
    value_set = len(set(value))
    print(parent)
    print(rank)
    return value_set

def main():
    n = 5
    computers = [[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,0],[0,1,0,1,1],[1,0,0,1,1]]
    print(solution(n, computers))

main()

# class DisjointSet :
#     def __init__(self, n) :
#         self.parent={}
#         self.rank={}
#         for i in range(n) :
#             self.parent[i] = i
#             self.rank[i] = 0
#     def Find(self,v) :
#         if self.parent[v] != v :
#             self.parent[v] = self.Find(self.parent[v])
#         return self.parent[v]
#     def Union(self, root1, root2) :
#         if self.rank[root1] > self.rank[root2] :
#             self.parent[root2] = root1
#         else :
#             self.parent[root1] = root2
#             if self.rank[root1] == self.rank[root2] :
#                 self.rank[root2] += 1