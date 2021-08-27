# 16926

def rotate(board, n):
    temp = [[0]*n for _ in range(n)]
    for x in range(n//2):
        N = x+n-1
        print(x, N)
        for i in range(x+1, N+1):
            print(i, x, N)
            temp[i][x] = board[i-1][x]
            temp[N][i] = board[N][i-1]
            temp[i-1][N] = board[i][N]
            temp[x][i-1] = board[x][i]
        n-=2
    return temp


# N, M, R = map(int, input().split())
# board = [[0]*M for _ in range(N)]

board = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

res = rotate(board, 4)
for r in res:
    print(r)