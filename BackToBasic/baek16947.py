from collections import deque
import sys

sys.setrecursionlimit(1000000)

N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(N):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

check = [0]*(N+1) # 0:방문 안했음, 1:방문했음, 2:사이클임

# return 정보 : # -1:사이클 못찾음, -2:사이클 찾았지만 포함 안됨, 1~N: 사이클 찾았고 시작인덱스
def get_cycle(x:int, p:int) -> int: # x:방문하려는 노드, p: 이전에 방문한 노드
    if check[x] == 1:  # x를 방문한 적이 있는데 또 방문하는 거면, 사이클을 찾은 것임
        return x       # 사이클의 시작 인덱스

    check[x] = 1            # x에 방문했음
    for y in graph[x]:      # x와 연결된 노드들 중에
        if y == p: continue # 직전 노드는 방문할 필요가 없음
        res = get_cycle(y, x)

        if res == -2:   # 사이클을 찾았지만 사이클에 포함되지 않는 노드라면
            return -2   # 그 이전에 방문했던 노드들도 -2로

        if res >= 0:       # 사이클을 찾았다면
            check[x] = 2   # 해당 노드는 check를 2로 해줌
            if x == res:   # res값은 사이클 시작 인덱스인데 현재 노드과 res가 같다면
                return -2  # 해당 노드는 이미 포함된 적이 있으므로 제외
            else:          # 그게 아니면,
                return res # 시작 인덱스를 이전에 방문했는 노드들에게도 알려줘야함.

    return -1 # 어떻게 해도 사이클이 없는 경우

get_cycle(1, 0)

answer = [-1]*(N+1)
need = deque()
for i in range(1, N+1):
    if check[i]==2:
        answer[i] = 0
        need.append(i)

while need:
    now = need.popleft()
    for n in graph[now]:
        if answer[n] == -1:
            need.append(n)
            answer[n] = answer[now]+1  # depth만 알면 됨.

print(*answer[1:], sep=' ')
