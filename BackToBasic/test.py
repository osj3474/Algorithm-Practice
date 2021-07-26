from copy import deepcopy as dc

N = int(input())
board = [list(map(lambda x:x, input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

MAX=0
origin_dic = {'C':0, 'P':0, 'Z':0, 'Y':0}
for i in range(N):
    width_dic = dc(origin_dic)
    height_dic = dc(origin_dic)
    for j in range(N):
        width_dic[board[i][j]]+=1
        height_dic[board[j][i]]+=1
    temp = max(width_dic.values())
    if MAX<temp: MAX=temp
    temp = max(height_dic.values())
    if MAX < temp: MAX = temp

for i in range(N):
    for j in range(N):
        # print('{}, {} 차례다'.format(i, j))
        for p in range(4):
            x = i + dx[p]
            y = j + dy[p]
            if x>=N or y>=N or x<0 or y<0: continue
            if board[i][j]==board[x][y]: continue
            board[i][j], board[x][y] = board[x][y], board[i][j]
            if i==x:
                # print('{}열 모두 검사'.format(j))
                # print('{}열 모두 검사'.format(y))
                temp1_dic = dc(origin_dic)
                temp2_dic = dc(origin_dic)
                for k in range(N):
                    temp1_dic[board[k][j]] += 1
                    temp2_dic[board[k][y]] += 1
                temp = max(temp1_dic.values())
                if MAX < temp: MAX = temp
                temp = max(temp2_dic.values())
                if MAX < temp: MAX = temp
            if j==y:
                # print('{}행 모두 검사'.format(i))
                # print('{}행 모두 검사'.format(x))
                temp1_dic = dc(origin_dic)
                temp2_dic = dc(origin_dic)
                for k in range(N):
                    temp1_dic[board[i][k]] += 1
                    temp2_dic[board[x][k]] += 1
                temp = max(temp1_dic.values())
                if MAX < temp: MAX = temp
                temp = max(temp2_dic.values())
                if MAX < temp: MAX = temp
            board[i][j], board[x][y] = board[x][y], board[i][j]

print(MAX)
