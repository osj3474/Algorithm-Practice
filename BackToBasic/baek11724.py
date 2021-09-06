from collections import defaultdict
import sys

N, M = map(int, sys.stdin.readline().split())
nodes = [i for i in range(1, N+1)]
group_lst = [0]*(N+1)
graph = defaultdict(list)
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

need, visited = [], set()
cnt = 1

for node in nodes:
    if node in visited: continue
    need.append(node)
    group_lst[node] = cnt
    while need:
        now = need.pop()
        if now in visited: continue
        need.extend(graph[now])
        visited.add(now)
        group_lst[now] = cnt
    cnt += 1

print(max(group_lst))