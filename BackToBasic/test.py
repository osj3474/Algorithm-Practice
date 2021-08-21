N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 인덱스가 0이면 북쪽,
# x=1, y=1
# x+dx[0] = 0 / y+dy[0] =1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0  # 청소 횟수

need = []  # 탐색할 좌표와 방향
need.append([r, c, d]) # 시작점(x좌표, y좌표, 방향)

while need:
    now = need.pop()
    x, y, d = now

    # 1. 현재 위치 청소한다.
    if board[x][y] == 0: cnt += 1  # 방문이 처음이라면 청소 +1
    board[x][y] = 1

    # 2. 현재 위치에서 왼쪽 방향부터 탐색
    left = (d + 3) % 4     # 왼쪽 방향
    isExistWay = False     # 네 방향 모두 불가한지 여부
    for i in range(4):     # 네 방향
        idx = (left-i) % 4
        newX = x + dx[idx]
        newY = y + dy[idx]

        if newX>0 or newY>0 or newX<N-1 or newY<M-1:  # 범위 안 벗어나고
            if board[newX][newY] == 1:   # 벽이나 이미 청소한 곳이 아니라면
                d = left                 # 그 방향으로 회전하고
                need.append([newX, newY, d])  # need에 넣어서 1번부터
                isExistWay = True        # 길은 있다.
            else:
                d = left    # 그 방향으로 회전하고
                continue    # 2번으로 돌아간다.

    if not isExistWay: # 네 방향 모두 불가한 경우
        print('')
