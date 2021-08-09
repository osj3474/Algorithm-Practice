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

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0]*N for _ in range(N)]
# d = N-1
#
# global cnt
# cnt = 0
#
# def go(i, j, visited):
#     global cnt
#     if (i, j) == (d, d):
#         # dp 업뎃이 필요함
#         print(1)
#         for p1, p2 in visited:
#             dp[p1][p2] += 1
#         visited = []
#         return
#     if dp[i][j] != 0:
#         cnt += dp[i][j]
#     dx = [board[i][j], 0]
#     dy = [0, board[i][j]]
#     for p in range(2):
#         x = i + dx[p]
#         y = j + dy[p]
#         if x>=0 and y>=0 and x<N and y<N:
#             if board[x][y] == 0: continue
#             visited.append((x, y))
#             go(x, y, visited)
#
# go(0,0,[])

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0]*N for _ in range(N)]
# d = N-1

# need, visited = [], []
# need.append((0, 0))
# visited.append((0, 0))
# while need:
#     now = need.pop()
#     i, j = now
#     print(now)
#     if (i, j) == (d, d):
#         print(visited)
#         for v1, v2 in visited:
#             dp[v1][v2] += 1
#         visited = []
#         print(visited)
#     if board[i][j] == 0: continue
#     if dp[i][j] != 0:
#         for v1, v2 in visited:
#             dp[v1][v2] += 1
#         visited = []
#     dx = [board[i][j], 0]
#     dy = [0, board[i][j]]
#     for p in range(2):
#         x = i + dx[p]
#         y = j + dy[p]
#         if x>=0 and y>=0 and x<N and y<N:
#             need.append((x, y))
#             visited.append((x, y))
#
# print(dp[d][d])

# 다앙햔 풀이법이 있을 수 있겠지만,
# 1x1 판일 때, (0,0) 으로 가는 경우의 수
# 2x2 판일 때, (1,1) 로 가는 경우의 수
# 3x3 판일 때, (2,2) 로 가는 경우의 수
# 이런식으로 구하기 시작하면, 나중에, nxn 판일 때,
# (n-1, n-1)로 가는 경우의 수를 구하는데, 이전꺼를 쓸 수 잇다.


# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0]*N for _ in range(N)]
# d = N-1

S = input().split()
N = len(S)
# my_dic = {'[]', '&', '*'}
for i in range(1, N):
    S[i] = S[i][:-1]
    temp = ''
    idx=0
    # print(S[i])
    j = len(S[i])-1
    while j>0:
        if S[i][j]=='&' or S[i][j]=='*':
            temp+=S[i][j]
            # print('{}라서 temp에 들어감. temp={}'.format(S[i][j], temp))
            j-=1
        elif S[i][j-1:j+1] == '[]':
            temp+=S[i][j-1:j+1]
            j-=2
            # print('{}라서 temp에 들어감. temp={}'.format(S[i][j], temp))
            # print('참고로 j={} 가 됐음.'.format(j))
        else:
            # print('{}인 상태로 나감.'.format(idx))
            break

    print(S[0]+temp, S[i][:j+1]+';')


