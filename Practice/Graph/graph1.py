from collections import defaultdict
from collections import deque

def solution(n, edges):
    node_lst = [float("Inf") for _ in range(n+1)]
    node_lst[0], node_lst[1] = 0, 0
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
    graph = dict(graph)

    queue = deque()
    queue.append(1)
    while queue:
        current = queue.popleft()
        for adj in graph[current]:
            if node_lst[adj] > node_lst[current]:
                if node_lst[adj] != node_lst[current]+1:
                    node_lst[adj] = node_lst[current]+1
                    queue.append(adj)
    MAX = max(node_lst)
    answer = node_lst.count(MAX)
    return answer


def main():
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))

main()


