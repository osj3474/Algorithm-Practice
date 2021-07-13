from collections import deque
from collections import defaultdict

N, M, V = map(int, input().split())
edge_dic = defaultdict(list)
for i in range(M):
    v1, v2 = map(int, input().split())
    edge_dic[v1].append(v2)
    edge_dic[v2].append(v1)

for key in edge_dic.keys():
    edge_dic[key].sort(reverse=True)

def DFS(graph, start):
    need, visited = list(), list()
    need.append(start)
    while need:
        now = need.pop()
        if now in visited: continue
        visited.append(now)
        need.extend(graph[now])
    return visited

def BFS(graph, start):
    need, visited = list(), list()
    need.append(start)
    while need:
        now = need.pop()
        if now in visited: continue
        visited.append(now)
        temp_lst = graph[now]
        temp_lst.extend(need)
        need = temp_lst
    return visited

DFS_result = DFS(edge_dic, V)
BFS_result = BFS(edge_dic, V)
for item in DFS_result:
    print(item, end=" ")
print()
for item in BFS_result:
    print(item, end=" ")


