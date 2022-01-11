M, N = map(int, input().split())
board = [[0]*N for _ in range(M)]

cnt = 0           # 꺾은선 갯수
fin = 1           # fin ==> M*N  ==> 종료
board[0][0] = 1

# 우(0), 하(1), 좌(2), 상(3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0     # 우(0) 로 시작

x, y = 0, 0
while fin<M*N:
    x += dx[d]
    y += dy[d]

    if (0<=x<M and 0<=y<N) and board[x][y]!=1:
        fin += 1
        board[x][y] = 1
    else:
        x -= dx[d]
        y -= dy[d]

        d = (d+1)%4
        cnt += 1

print(cnt)