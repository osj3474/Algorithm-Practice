from collections import deque

N, K = map(int, input().split())

need = deque()
need.append(N)
MAX = max(N, K)*2+1
dist = [-1]*MAX
prev_lst = [-1]*MAX
visited = [0]*MAX
dist[N] = 0

while need:
    now = need.popleft()
    if now == K: break
    for n in [now-1, now+1, now*2]:
        if 0<=n<MAX and visited[n]==0:
            need.append(n)
            visited[n]=1
            prev_lst[n]=now
            dist[n] = dist[now]+1

if N==K:
    print(0)
    print(N)

else:
    print(dist[K])
    answer_lst = [0]*(dist[K]+1)
    answer_lst[-1]=K
    i = 2
    n = K
    while True:
        prev = prev_lst[n]
        if prev == N:
            answer_lst[-i]=prev
            break
        answer_lst[-i]=prev
        n = prev
        i += 1

    for p in answer_lst:
        print(p, end=' ')
