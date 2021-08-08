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

