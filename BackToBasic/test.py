N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
com_lst = list(map(int, input().split()))
rotate = [[0,0,0,0,0], [0,3,4,2,5], [0,3,4,6,1], [0,6,1,2,5], [0,1,6,2,5], [0,3,4,1,6], [0,3,4,5,2]]
dice = [0]*7
front = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
idx = 6

def checkZero(x, y, idx):
    if board[x][y]==0:
        board[x][y] = dice[idx]
    else:
        dice[idx] = board[x][y]
        board[x][y] = 0

for i in com_lst:
    if i==1 and y+1>=N: continue
    elif i==2 and y-1<0: continue
    elif i==3 and x-1<0: continue
    else:
        if x+1>=N: continue
    idx = rotate[idx][i]
    checkZero(x, y, idx)
    print(dice[front[idx]])
