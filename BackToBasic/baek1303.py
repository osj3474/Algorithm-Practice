N, M = map(int, input().split())
board = [input() for _ in range(M)]

dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
cnt_dic = dict()
cnt_dic['W']=0
cnt_dic['B']=0

check_lst=[[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if check_lst[i][j] != 0: continue
        need = list()
        need.append((i, j))
        cnt = 0
        team = board[i][j]
        while need:
            n, m = need.pop()
            if check_lst[n][m] != 0: continue
            check_lst[n][m]=1
            cnt+=1
            for p in range(4):
                x=n+dx[p]
                y=m+dy[p]
                if x>=M or y>=N or x<0 or y<0: continue
                if board[x][y]!=team:continue
                need.append((x, y))
                # print('    {}, {}에서 {}, {} 추가해줫음. 그래서 현재 need는 {}임'.format(n, m, x, y, need))
        cnt_dic[team] += cnt*cnt
        # print('{},{}에서 cnt가 {}라서, 최종 {}팀의 합은 {}입니다.'.format(i, j, cnt, team, cnt_dic[team]))

print(cnt_dic['W'], cnt_dic['B'])
