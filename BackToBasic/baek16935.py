N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command_lst = list(map(int, input().split()))

def operate(board, com: int):
    N, M = len(board), len(board[0])
    x = 0
    temp = [[0] * M for _ in range(N)]
    if com==1:
        for i in range(N-1, -1, -1):
            y = 0
            for j in range(M):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        board = temp
    elif com==2:
        for i in range(N):
            y = 0
            for j in range(M-1, -1, -1):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        board = temp
    elif com==3:
        temp = [[0] * N for _ in range(M)]
        for j in range(M):
            y = 0
            for i in range(N-1, -1, -1):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        board = temp
    elif com==4:
        temp = [[0] * N for _ in range(M)]
        for j in range(M-1,-1,-1):
            y = 0
            for i in range(N):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        board = temp
    elif com==5:
        x = 0
        for i in range(N//2):
            y = M//2
            for j in range(M//2):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        x = N//2
        for i in range(N//2):
            y = M//2
            for j in range(M//2, M):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        x = N//2
        for i in range(N//2, N):
            y = 0
            for j in range(M//2, M):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        x = 0
        for i in range(N//2, N):
            y = 0
            for j in range(M//2):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        board = temp
    elif com==6:
        x = N//2
        for i in range(N//2):
            y = 0
            for j in range(M//2):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        x = 0
        for i in range(N//2):
            y = 0
            for j in range(M//2, M):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        x = 0
        for i in range(N//2, N):
            y = M//2
            for j in range(M//2, M):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        x = N//2
        for i in range(N//2, N):
            y = M//2
            for j in range(M//2):
                temp[x][y] = board[i][j]
                y += 1
            x += 1
        board = temp
    return board


for com in command_lst:
    board = operate(board, com)

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end=' ')
    print()
