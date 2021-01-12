# def solution(n, costs):
#     tree = set()
#     costs = sorted(costs, key=lambda x:x[2])
#     total = 0
#     for cost in costs:
#         if cost[0] in tree and cost[1] in tree:  # 이게 사이크 체크 아닌가 --> Disjointset이 2개 생기면, set에는 다 들어가 있는데, 전체 연결이 안됨.
#             continue
#         tree.add(cost[0])
#         tree.add(cost[1])
#         total += cost[2]
#     return total


def Find(v, parent) : # v의 parent를 찾는 함수
    print('Find 진입')
    print("v:", v, "parent:", parent)
    if parent[v] != v :
        parent[v] = Find(parent[v], parent)
    print("반환 값:", parent[v])
    return parent[v]

def Union(x, y, parent, rank) :  # x, y를 연결하는 함수
    print("Union 진입")
    print("x:",x)
    print("y:",y)
    print("parent:",parent)
    print("rank:", rank)
    if rank[x] > rank[y] :
        parent[y] = x
    elif rank[x] < rank[y] :
        parent[x] = y
    else :
        if y == 3:
            print(parent[y])
            print(x)
        parent[y] = x
        rank[x] += 1
    return parent, rank

def solution(n, costs):
    parent = {}
    rank = {}
    # Make set
    for i in range(n) :
        parent[i] = i
        rank[i] = 0

    # costs = sorted(costs, key=lambda x:x[2])
    total = 0
    for cost in costs:
        print("#############시작##############")
        print("cost값이 {}입니다".format(cost))
        # one, other, pay = cost
        # print(one, other, pay)
        one, other = cost
        if Find(one, parent) != Find(other, parent):
            parent, rank = Union(one, other, parent, rank)
            # total += pay
    print(parent)
    print(rank)
    return total

def main():
    n = 5
    # costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    costs = [[0,1], [0,2], [1,3], [3,4]]
    print(solution(n, costs))


main()
#
# node_lst = [[0,1], [0,2], [3,4], [1,3]]
#
# parent = {}
# rank = {}
# # Make set
# for i in range(5) :
#     parent[i] = i
#     rank[i] = 0
#
# for node in node_lst:
#     if Find(node[0], parent) != Find(node[1], parent):
#         Union(node[0], node[1], parent, rank)
#
# for i in range(5) :
#     root = Find(i, parent)
#     parent[i] = root
#
#
# print(parent)
# print(rank)
#


