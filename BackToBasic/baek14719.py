# H, W = 4, 4
# cnt_lst = [3, 0, 1, 4]
H, W = map(int, input().split())
cnt_lst = list(map(int, input().split()))
board = [[0]*W for _ in range(H)]

for i in range(H-1, -1, -1):
    for j in range(W):
        if cnt_lst[j]>0:
            board[i][j]=1
            cnt_lst[j]-=1

cnt = 0
for i in range(H):
    temp = 0
    for j in range(W):
        if board[i][j] == 1:
            for p in range(j+1, W):
                if board[i][p] == 0: temp+=1
                else: cnt+=temp; temp=0
            break

print(cnt)

