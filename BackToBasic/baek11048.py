# import sys     # 결과 => 시간 초과
# sys.setrecursionlimit(1000000)
#
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# global MAX
# MAX = 0
#
# def go(x, y, cnt):
#     global MAX
#     cnt += board[x][y]
#     if (x, y)==(N-1, M-1) and MAX<cnt:
#         MAX = cnt
#
#     for mx, my in [(x+1, y), (x, y+1), (x+1, y+1)]:
#         if mx>=N or my>=M: continue
#         go(mx, my, cnt)
#
# go(0, 0, 0)
# print(MAX)




# import sys      # 결과 => 메모리 초과
# sys.setrecursionlimit(1000000)
#
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# dp = [[0]*M for _ in range(N)]
# dp[0][0] = board[0][0]
#
# n, m = N-1, M-1
#
# def go(x, y, cnt):
#     cnt += board[x][y]
#     if dp[x][y]>cnt: return
#     dp[x][y] = cnt
#     if (x, y)==(n, m): return
#
#     for mx, my in [(x+1, y), (x, y+1), (x+1, y+1)]:
#         if mx>=N or my>=M: continue
#         go(mx, my, cnt)
#
# go(0, 0, 0)
# print(dp[n][m])


# import sys      # 결과 => 시간 초과
#
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# dp = [[-1]*M for _ in range(N)]
# dp[0][0] = board[0][0]
#
# need = []
# need.append((0, 0))
# while need:
#     i, j = need.pop()
#     for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]:
#         if x>=N or y>=M: continue
#         cnt = dp[i][j]+board[x][y]
#         if dp[x][y] < cnt:
#             dp[x][y] = cnt
#             need.append((x, y))
#
# print(dp[N-1][M-1])


import sys      # 정답

N, M = map(int, sys.stdin.readline().split())
board = [[0]*(M+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + board[i][j]

print(dp[N][M])