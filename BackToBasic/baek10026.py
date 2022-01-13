N = int(input())
A = [list(input()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def find_group(A):
    cnt = 0
    ck = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if ck[i][j] == 1:
                continue

            need = list()
            need.append([i, j])
            while need:
                cx, cy = need.pop()
                for p in range(4):
                    x = cx + dx[p]
                    y = cy + dy[p]

                    if 0 <= x < N and 0 <= y < N and ck[x][y] == 0 and A[x][y] == A[cx][cy]:
                        ck[x][y] = 1
                        need.append([x, y])
            cnt += 1
    return cnt


B = [[''] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] == 'R' or A[i][j] == 'G':
            B[i][j] = 'SAME'
        else:
            B[i][j] = A[i][j]

print(find_group(A), find_group(B))