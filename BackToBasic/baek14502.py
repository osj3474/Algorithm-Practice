from copy import deepcopy as dp

N, M = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def find_zone(a):
    for i in range(N):
        for j in range(M):
            if a[i][j] != 2: continue

            need = set()
            need.add((i, j))
            while need:
                x, y = need.pop()
                for p in range(4):
                    cx = x+dx[p]
                    cy = y+dy[p]
                    if 0<=cx<N and 0<=cy<M and a[cx][cy]==0:
                        a[cx][cy] = 2
                        need.add((cx, cy))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 0:
                cnt += 1

    return cnt

board = [list(map(int, input().split())) for _ in range(N)]

flst = []

for i in range(N):
    for j in range(M):
        if board[i][j]==0:
            flst.append((i, j))

n = len(flst)
MAX = 0
for i in range(n-2):  # 모든 경우에 대해서 벽을 세운다.
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            for x, y in [flst[i], flst[j], flst[k]]:
                board[x][y] = 1

            _max = find_zone(dp(board))

            if MAX < _max: MAX = _max
            for x, y in [flst[i], flst[j], flst[k]]:
                board[x][y] = 0

print(MAX)