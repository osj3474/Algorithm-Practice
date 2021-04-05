from collections import defaultdict

N, M, V = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

graph_dic = defaultdict(set)
for node in graph:
    graph_dic[node[0]].add(node[1])
    graph_dic[node[1]].add(node[0])

def DFS(graph, start):
    visited = []
    need = []
    need.append(start)
    while need:
        now = need.pop()
        if now not in visited:
            need.extend(reversed(list(graph[now])))
            visited.append(now)
    return visited

def BFS(graph, start):
    visited = []
    need = []
    need.append(start)
    while need:
        now = need.pop(0)
        if now not in visited:
            need.extend(list(graph[now]))
            visited.append(now)
    return visited

print(graph_dic)
print(DFS(graph_dic, V))
print(BFS(graph_dic, V))