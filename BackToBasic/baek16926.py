# 첫 시도  ==> 실패

# from copy import deepcopy as dp
#
# def rotate(board, x, n, m):
#     temp = dp(board)
#     N = n - 1
#     M = m - 1
#     for i in range(x+1, N+1):
#         temp[i][x] = board[i-1][x]
#         temp[i-1][M] = board[i][M]
#     for i in range(x+1, M+1):
#         temp[N][i] = board[N][i - 1]
#         temp[x][i - 1] = board[x][i]
#     return temp
#
# N, M, R = map(int, input().split())
# board = [list(map(int ,input().split())) for _ in range(N)]
#
# MIN = min(N, M)
# for x in range(MIN//2):
#     d = (N + M - 2) * 2
#     cnt = R % d
#     for _ in range(cnt):
#         board = rotate(board, x, N, M)
#     N -= 1
#     M -= 1
#
# N = len(board)
# M = len(board[0])
# for i in range(N):
#     for j in range(M):
#         print(board[i][j], end=' ')
#     print()

# 두번째 시도  ===> 성공
N, M, R = map(int, input().split())
board = [list(map(int ,input().split())) for _ in range(N)]
MIN = min(N, M)//2   # 그룹수
group_lst = [[] for _ in range(MIN)]


# 테두리 기준으로 그룹을 지음
n, m = N-1, M-1
for x in range(MIN):
    for i in range(x, m):
        group_lst[x].append(board[x][i])
    for i in range(x, n):
        group_lst[x].append(board[i][m])
    for i in range(m, x, -1):
        group_lst[x].append(board[n][i])
    for i in range(n, x, -1):
        group_lst[x].append(board[i][x])
    n -= 1
    m -= 1

# rotate
for i in range(MIN):
    length = len(group_lst[i])
    temp = [0]*length
    for j in range(length):
        temp[j] = group_lst[i][(j+R)%length]
    group_lst[i] = temp

# 다시 채워넣음
n, m = N-1, M-1
for x in range(MIN):
    idx = 0
    group = group_lst[x]
    for i in range(x, m):
        board[x][i] = group[idx]
        idx+=1
    for i in range(x, n):
        board[i][m] = group[idx]
        idx+=1
    for i in range(m, x, -1):
        board[n][i] = group[idx]
        idx += 1
    for i in range(n, x, -1):
        board[i][x] = group[idx]
        idx += 1
    n -= 1
    m -= 1


for i in range(N):
    for j in range(M):
        print(board[i][j], end=' ')
    print()
