from collections import deque

N, K = map(int, input().split())
need = deque()
need.append(N)

visited = list()
cnt = 0
while need:
    if K in need: break
    new = list()
    for item in list(need):
        n = need.popleft()
        if n in visited: continue
        visited.extend([n-1, n+1, n*2])
        new.extend([n-1, n+1, n*2])
    need = deque(new)
    cnt += 1
print(cnt)
