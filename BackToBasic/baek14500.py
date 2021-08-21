N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

p_lst = [
    [[1,1,1,1]],
    [[1],[1],[1],[1]],

    [[1,1],[1,1]],

    [[1,0],[1,0],[1,1]],
    [[1,1,1],[1,0,0]],
    [[1,1],[0,1],[0,1]],
    [[0,0,1],[1,1,1]],
    [[0,1],[0,1],[1,1]],
    [[1,0,0],[1,1,1]],
    [[1,1],[1,0],[1,0]],
    [[1,1,1],[0,0,1]],

    [[1,0],[1,1],[0,1]],
    [[0,1,1],[1,1,0]],
    [[0,1],[1,1],[1,0]],
    [[1,1,0],[0,1,1]],

    [[1,1,1],[0,1,0]],
    [[1,0],[1,1],[1,0]],
    [[0,1,0],[1,1,1]],
    [[0,1],[1,1],[0,1]]
]

MAX = 0
for x in range(N):
    for y in range(M):
        for p in p_lst:
            n = len(p)
            m = len(p[0])
            cnt = 0
            if x+n-1<N and y+m-1<M:  # 시작점 기준으로 가능한지 판단
                # print('p={}, 시작점={},{}'.format(p, x, y))
                for i in range(n):
                    for j in range(m):
                        if p[i][j]==0: continue
                        cnt += board[x+i][y+j]
                        # print('     cnt에 {}를 더했더니 {}가 됨.'.format(board[x+i][y+j], cnt))
            if MAX < cnt:
                # print('p={}, 시작점={},{}일때, MAX업뎃'.format(p, x, y))
                MAX = cnt

print(MAX)