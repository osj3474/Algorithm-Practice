N = int(input())
board = [list(input()) for _ in range(N)]

def find_max_value(lst):
    M, cnt = 1, 1
    for i in range(1, N):
        if lst[i-1] == lst[i]:
            cnt += 1
            if M<cnt: M=cnt
        else:
            cnt = 1
    return M

MAX = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(N):
        cur = board[i][j]
        for p in range(4):
            x = i + dx[p]
            y = j + dy[p]
            if x>=0 and y>=0 and x<N and y<N:
                if cur != board[x][y]:
                    board[i][j], board[x][y] = board[x][y], board[i][j]
                    vert_lst = list(map(list, list(zip(*board))))
                    for k in range(N):
                        MAX = max(MAX, find_max_value(board[k]), find_max_value(vert_lst[k]))
                    board[i][j], board[x][y] = board[x][y], board[i][j]

print(MAX)