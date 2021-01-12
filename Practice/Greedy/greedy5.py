# def Find(v, parent) :
#     if parent[v] != v :
#         parent[v] = Find(parent[v], parent)
#     return parent[v]
# def Union(x, y, parent, rank) :
#     if rank[x] > rank[y] :
#         parent[y] = x
#     elif rank[x] < rank[y] :
#         parent[x] = y
#     else :
#         parent[y] = x
#         rank[x] += 1
#     return parent, rank
#
# def solution(n, costs):
#     parent = {}
#     rank = {}
#     # Make set
#     for i in range(n) :
#         parent[i] = i
#         rank[i] = 0

def solution(n, costs):
    tree = set()
    costs = sorted(costs, key=lambda x:x[2])
    total = 0
    for cost in costs:
        if cost[0] in tree and cost[1] in tree:
            continue
        tree.add(cost[0])
        tree.add(cost[1])
        total += cost[2]
    return total

def main():
    n = 5
    costs = [[0,1,1],[0,2,2],[1,3,4],[3,4,3],[1,2,5],[2,4,6]]
    print(solution(n, costs))


main()
