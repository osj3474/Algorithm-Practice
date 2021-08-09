# # #1890
# # # DFS/BFS
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# dp = [[0]*N for _ in range(N)]
# need, prev = [], []
# need.append((0,0))
# d = N-1
#
# cnt = 0
# while need:
#     now = need.pop()
#     i, j = now
#     if (i, j) != (0,0):
#         prev.append(now)
#     if dp[i][j]==1:
#         cnt += 1
#         continue
#     if (i, j)== (d, d):
#         cnt += 1
#         for p1, p2 in prev:
#             dp[p1][p2] = 1
#         prev = []
#         continue
#     dx = [board[i][j], 0]
#     dy = [0, board[i][j]]
#     for p in range(2):
#         x = i+dx[p]
#         y = j+dy[p]
#         if x>=0 and y>=0 and x<N and y<N:
#             need.append((x, y))
#
# print(cnt)

# 2616
# from itertools import combinations as cb
#
# N = int(input())
# car_lst = list(map(int, input().split()))
# k = int(input())
#
# dp = [0]*(N-k)
# dp[0] = sum(car_lst[:k])
# for i in range(1, N-k):
#     dp[i] = dp[i-1]-car_lst[i-1]+car_lst[i+k]
#
# lst = list(cb(dp, 3))
# print(lst)

# dp[i][j] = 세로가 i인 우리'[;p;;에서 사자를 넣는 경우의 수
# j : 가장 최근 칸의 배치 종류
# j가 0이면, 사자를 배치하지 않은 경우
# j가 1이면, 사자가 왼쪽에 배치된 경우
# j가 2이면, 사자가 오른쪽에 배치된 경우
# dp[i][0] =

# N = int(input())
# answer = 0
# mod = 9901
# dp = [[0]*3 for _ in range(N+1)]

# n = int(input())
# fodo = [int(input()) for _ in range(n)]



# global MAX
# MAX = 0
#
# def drink(d, s, prev):
#     global MAX
#     if d==n-1:
#         if MAX<s:
#             print(prev)
#             MAX=s
#         return
#     if d>n: return
#     if len(prev)>=2:
#         if d-1==prev[-2] and d-2==prev[-1]:
#             drink(d+1, s, prev)
#             return
#     drink(d + 1, s, prev)
#     prev.append(d)
#     drink(d + 1, s + fodo[d], prev)
#
# # prev = list()
# drink(0, 0, list())
#
# print(MAX)

N, K = map(int, input().split())
w, v = [0]*N, [0]*N
for i in range(N):
    w[i], v[i] = map(int, input().split())

# dp[i][j] = i번째 까지의 물건 안에서, 캐파가 j만큼 남았을 때의 최대 가치
# 궁극적으로 원하는 건 = dp[N][K] 이다.
# 생각은 l, m을 본다고 했을 때, 이전에 어떤 물건을 샀는지는 생각도 하지 않고,
# 딱 그 순간 i번째 물건을 살지 안 살지만 결정하고,
# 산다면, i를 제외하기 위해 i-=1 하고, 캐파도 w[i] 만큼해야한다.
# 안산다 하더라도, i는 제외이고(i-=1), 캐파는 변동 없다.
# 만약, 애초에 i번째 물건이 나의 모든 캐파를 가지고도 못 사는 거였다면,
# 그냥 바로 윗칸 꺼(i번째 물건이 없다고 했을 때의 최대 가치이니까.)를 받자.

dp = [[0]*(K+1) for _ in range(N)]
for i in range(N):
    for j in range(1, K+1):
        # 기본적으로 캐파가 허락해줘야한다.
        if j>=w[i]:
            # 산다/안산다 는 더 높은 가치로 판단
            # 비교는 바로 윗칸이다. 왜냐하면,
            # 캐파가 늚으로써 물건 선택지가 바뀌었을 수도 있기 때문이다.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][K])

