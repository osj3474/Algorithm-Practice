# 16926

def rotate(board, n, m):
    temp = [[0]*m for _ in range(n)]
    MIN = min(n, m)
    for x in range(MIN//2):
        N = x+n-1
        M = x+m-1
        # print(x, N)
        for i in range(x+1, N+1):
            # print(i, x, N)
            temp[i][x] = board[i-1][x]
            temp[N][i] = board[N][i-1]
            temp[i-1][N] = board[i][N]
            temp[x][i-1] = board[x][i]
        for i in range(x+1, M+1):
            print()
        n-=2
    return temp


# N, M, R = map(int, input().split())
# board = [list(map(int ,input().split())) for _ in range(N)]

N, M, R = 2, 3, 2
board = [[1,2,3], [4,5,6]]

for _ in range(R):
    board = rotate(board, N, M)

# for i in range(N):
#     for j in range(M):
#         print(board[i][j], end=' ')
#     print()
print(board)