from collections import deque

M, N = map(int, input().split())
board = [input() for _ in range(N)]
dist = [[-1]*M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

need = deque()
need.append((0, 0))
dist[0][0] = 0
while need:
    i, j = need.popleft()
    for p in range(4):
        x = i + dx[p]
        y = j + dy[p]
        # print('{},{} 가려고 하는데'.format(x, y))
        if x>=0 and y>=0 and x<N and y<M:
            if dist[x][y] == -1:
                if board[x][y] == '1':
                    dist[x][y] = dist[i][j] + 1
                    # for d in dist:
                    #     print(d)
                    need.append((x, y))
                else:
                    dist[x][y] = dist[i][j]
                    need.appendleft((x, y))
                    # for d in dist:
                    #     print(d)

print(dist[N-1][M-1])