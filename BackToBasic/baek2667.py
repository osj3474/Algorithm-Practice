N = int(input())
board = [input() for _ in range(N)]

parent = [[0]*N for _ in range(N)]
cnt_info = [0]*(N*N)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

cnt = 1
for i in range(N):
    for j in range(N):
        if board[i][j]=='0' or parent[i][j]!=0: continue
        need = []
        need.append((i, j))
        while need:
            now = need.pop()
            curX, curY = now
            if parent[curX][curY]!=0: continue
            parent[curX][curY] = cnt
            cnt_info[cnt] += 1
            for p in range(4):
                x = curX + dx[p]
                y = curY + dy[p]
                if x>=0 and y>=0 and x<N and y<N:
                    if board[x][y]=='0': continue
                    need.append((x, y))
        cnt += 1

result = cnt_info[1:cnt]
result.sort()
print(cnt-1)
for r in result:
    print(r)

