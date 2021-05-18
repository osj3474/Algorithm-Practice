from collections import defaultdict

N = int(input())
A = [[0]*N for _ in range(N)]
for i in range(N):
    string = input()
    for j in range(N):
        A[i][j] = string[j]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

MAX = 0
for i in range(N):
    for j in range(N):
        for p in range(4):
            x = i + dx[p]
            y = j + dy[p]
            if x<0 or x>=N or y<0 or y>=N: continue
            if A[i][j] != A[x][y]:
                line_lst = [defaultdict(int) for _ in range(4)]
                A[i][j], A[x][y] = A[x][y], A[i][j]
                for k in range(N):
                    line_lst[0][A[i][k]] += 1
                    line_lst[1][A[x][k]] += 1
                    line_lst[2][A[k][j]] += 1
                    line_lst[3][A[k][y]] += 1
                for k in range(4):
                    temp = max(line_lst[k].items())[1]
                    if MAX < temp:
                        MAX = temp
                A[x][y], A[i][j] = A[i][j], A[x][y]
print(MAX)