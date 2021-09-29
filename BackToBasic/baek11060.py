import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

need = deque()
dist = [-1]*N
dist[0] = 0
fin = N-1

need.append(0)
while need:
    n = need.popleft()
    if n+A[n] >= fin:            # 목표지점 도달 가능 조건
        answer = dist[n]+1       # 현재 지점에서 1 더한 값이 정답이지만,
        for i in range(n+1, N):  # dist 를 마무리 함.
            dist[i] = answer
        break


    for i in range(n, n+A[n]+1):
        # or 뒤의 조건이 중요. 거리를 계산 해보고 더 비용이 낮으면 업데이트 가능.
        if i<N and A[i]!=0 and (dist[i]==-1 or dist[i]>dist[n]+1):
            need.append(i)
            dist[i] = dist[n] + 1

print(dist[N-1])