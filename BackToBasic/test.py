def rotate(board, n, m, cnt):
    temp = [[0]*m for _ in range(n)]
    MIN = min(n, m)
    N = n - 1
    M = m - 1
    idx_lst = [0] * (n * m)
    for x in range(MIN//2):   # 10^8
        idx = 0
        # for i in range(x, n):
        #     idx_lst[idx] = (i, x)
        #     idx += 1
        # for i in range(x, m):
        #     idx_lst[idx] = (N, i)
        #     idx += 1
        # for i in range(M, -1, -1):
        #     idx_lst[idx] = (i, M)
        #     idx += 1
        # for i in range(M-1, 0, -1):
        #     idx_lst[idx] = (x, i)

        N -= 1
        M -= 1
    return temp

N, M, R = map(int, input().split())
board = [list(map(int ,input().split())) for _ in range(N)]

# for _ in range(R):
board = rotate(board, N, M, R)

# for i in range(N):
#     for j in range(M):
#         print(board[i][j], end=' ')
#     print()
print(board)