# find는 해당 노드의 부모를 찾는 것임.
def Find(v, parent):
    if parent[v] != v: parent[v] = Find(parent[v], parent)
    return parent[v]

def Union(x, y, parent, rank):
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1
    return parent, rank


def solution(n, computers):
    # 일단 기본적으로 각 노드의 부모가 누구인지를 담는 딕셔너리와 해당 노드에 이어진 것에 대한 height가 필요함.
    parent = {}
    rank = {}
    # 초기화를 일단 해준다.
    for i in range(n):
        parent[i] = i  # 처음 각 노드의 부모는 자기자신
        rank[i] = 0    # 연결된 거는 아무것도 없으니까 모두 0

    for i in range(len(computers)):
        for edge in range(len(computers[i])):
            if edge == i:
                continue
            if computers[i][edge] == 1:
                v1 = i
                v2 = edge
                x = Find(v1, parent)
                y = Find(v2, parent)
                if x != y:
                    parent, rank = Union(x, y, parent, rank)

    for i in range(n):
        root = Find(i, parent)
        parent[i] = root

    value = []
    value = list(parent.values())
    value_set = len(set(value))
    return value_set

def main():
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))

main()