from collections import defaultdict
from collections import deque
import sys

K = int(input())

answer_lst = []
for _ in range(K):
    answer = True
    graph = defaultdict(list)
    V, E = map(int, sys.stdin.readline().split())
    for _ in range(E):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    color = [-1]*(V+1)
    need, visited = deque(), set()
    for k in graph.keys():
        need.append(k)
        color[k]=True
        break
    while need:
        now = need.popleft()
        if now in visited:
            if not need and len(visited) != V:
                for k in graph.keys():
                    if k in visited: continue
                    need.append(k)
                    break
            continue
        visited.add(now)
        for v in graph[now]:
            if color[v] == -1:                 # 한번도 방문 안했으면
                color[v] = color[now] ^ True   # 지금과 toggle된 색을 칠하고
            elif color[v] == color[now]:       # 방문한 적 있는데, 지금의 색이랑 같으면
                answer = False                 # 탈락
                break
        if answer==False: break
        need.extend(graph[now])

    if answer == False: print("NO")
    else: print("YES")
