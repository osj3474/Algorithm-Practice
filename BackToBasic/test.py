from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]

cnt = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# limit = 20
dist = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

need = deque()
need.append((0, 0))
dist[0][0] = 1
visited[0][0] = True
while need:
    now = need.popleft()
    i, j = now
    for p in range(4):
        x = i + dx[p]
        y = j + dy[p]
        if x >= 0 and y >= 0 and x < N and y < M:
            if board[x][y] == '0' or visited[x][y]==True: continue
            need.append((x, y))
            dist[x][y] = dist[i][j] + 1
            visited[x][y] = True
            # print('{}, {} 는 방문을 햇습니당~'.format(x, y))
            # limit -= 1
            # if limit<0: break
    # if limit < 0: break


print(dist[N-1][M-1])
