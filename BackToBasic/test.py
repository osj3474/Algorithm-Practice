from copy import deepcopy as dc

N = int(input())
board = [list(map(lambda x:x, input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

MAX=0

def getRowMAX(board, N, r):
    MAX = 0
    prev = board[r][0]
    cnt = 1
    for i in range(1, N):
        cur = board[r][i]
        if prev==cur:
            cnt+=1
            if MAX < cnt: MAX = cnt
        else:
            prev = cur
            if MAX < cnt: MAX = cnt
            cnt = 1
    return MAX

def getColMAX(board, N, c):
    MAX = 0
    prev = board[0][c]
    cnt = 1
    for i in range(1, N):
        cur = board[i][c]
        if prev==cur:
            cnt+=1
            if MAX < cnt: MAX = cnt
        else:
            prev = cur
            if MAX < cnt: MAX = cnt
            cnt = 1
    return MAX

# board[2][1], board[2][2] = board[2][2], board[2][1]
# print(getColMAX(board,N,2))

# for i in range(N):
#     MAX = max(MAX, getRowMAX(board, N, i), getColMAX(board, N, i))

for i in range(N):
    for j in range(N):
        print('{}, {} 차례다'.format(i, j))
        for p in range(4):
            x = i + dx[p]
            y = j + dy[p]
            if x>=N or y>=N or x<0 or y<0: continue
            if board[i][j]==board[x][y]: continue
            board[i][j], board[x][y] = board[x][y], board[i][j]
            for now in range(N):
                print(board[now])
            for k in range(N):
                MAX = max(getColMAX(board, N, k), getColMAX(board, N, k))
            board[i][j], board[x][y] = board[x][y], board[i][j]

print(MAX)


class Person():
    def __init__(self, count):
        self.count = count
    def addCnt(self):
        self.count += 1


