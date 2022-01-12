from collections import deque

N, K = map(int, input().split())

_max = 100000
ck = [_max] * (_max + 1)
ck[N] = 0

need = deque()
need.append([N, 0])  # (현재위치, 이동횟수)
ck[N] = 0
while need:
    x, cnt = need.popleft()
    if x == K:       # 종료 조건
        break

    # 1) +1이동 (1초 소요)
    n = x+1
    if n<=_max and cnt+1 <= ck[n]:
        ck[n] = cnt+1
        need.append([n, cnt+1])

    # 2) -1이동 (1초 소요)
    n = x-1
    if 0<=n and cnt+1 <= ck[n]:
        ck[n] = cnt+1
        need.append([n, cnt+1])

    # 3) *2이동 (0초 소요)
    n = x*2
    if n<=_max:
        ck[n] = cnt
        need.append([n, cnt])

print(ck[K])