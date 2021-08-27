# 16926

def rotate(board, n):
    temp = [[0]*n for _ in range(n)]
    for x in range(n//2):
        N = x+n-1
        for i in range(1, n):
            temp[i][x] = board[i-1][x]
            temp[x][i] = board[N][i-1]
            temp[i][N] = board[i+1][N]
            temp[x][i] = board[x][i+1]
        n-=2
    return temp


N, M, R = map(int, input().split())
board = [[0]*M for _ in range(N)]
