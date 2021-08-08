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

# dp[n] = n개 카드 구매 최대 비용
# = max(dp[n-1]+p[1], dp[n-2]+p[2], ...)

# dp[i][j] = i를 1,2,3의 합으로 나타내는 경우의 수, 마지막 사용한 수 j
n = int(input())
num_lst = [int(input()) for _ in range(n)]
MAX = max(num_lst)
k = 1000000009
dp = [[0]*4 for _ in range(MAX+1)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, MAX+1):
    dp[i][1] = dp[i-1][2]%k+dp[i-1][3]%k
    dp[i][2] = dp[i-2][1]%k+dp[i-2][3]%k
    dp[i][3] = dp[i-3][1]%k+dp[i-3][2]%k

for i in num_lst:
    print((dp[i][1]+dp[i][2]+dp[i][3])%k)
