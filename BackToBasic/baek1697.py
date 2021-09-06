from collections import deque

N, K = map(int, input().split())
visited = [0]*200001
need, next_level, new_visited = deque(), list(), list()
need.append(N)

cnt = 0
while need:
    now = need.popleft()
    if now == K: break
    new_visited.append(now)
    for k in [now-1, now+1, now*2]:
        if 1<=k<200001 and visited[k]==0:
            next_level.append(k)
    if not need:
        need = deque(next_level)
        for n in new_visited:
            visited[n]=1
        next_level.clear()
        new_visited.clear()
        cnt += 1

print(cnt)
