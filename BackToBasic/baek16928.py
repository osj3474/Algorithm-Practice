# from collections import deque   # 정답이지만, 코드 리팩토링 가능
#
# FIN = 100
#
# N, M = map(int, input().split())
# sl = [0]*(FIN+1)
#
# for _ in range(N+M):
#     x, y = map(int, input().split())
#     sl[x] = y
#
# need = deque()
# need.append(1)
# dist = [-1]*(FIN+1)
# dist[1] = 0
#
# while need:
#     n = need.popleft()
#
#     if n==FIN:
#         break
#     if n>100: continue
#
#     if sl[n] != 0:
#         if dist[sl[n]] == -1 or dist[sl[n]] > dist[n]:
#             need.append(sl[n])
#             dist[sl[n]] = dist[n]
#         continue
#
#     for i in range(1, 7):
#         idx = n+i
#         if idx > 100: continue
#
#         cost = dist[n] + 1
#         if dist[idx]==-1 or dist[idx]>cost:
#             need.append(idx)
#             dist[idx] = cost
#
# print(dist[FIN])



from collections import deque

FIN = 100

N, M = map(int, input().split())
sl = list(range(FIN+1))

for _ in range(N+M):
    x, y = map(int, input().split())
    sl[x] = y

need = deque()
need.append(1)
dist = [-1]*(FIN+1)
dist[1] = 0

while need:
    n = need.popleft()

    for i in range(1, 7):
        idx = n+i
        if idx > 100: continue

        idx = sl[idx]
        if dist[idx]==-1:
            need.append(idx)
            dist[idx] = dist[n] + 1

print(dist[FIN])