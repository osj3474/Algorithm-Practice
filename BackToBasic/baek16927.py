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
