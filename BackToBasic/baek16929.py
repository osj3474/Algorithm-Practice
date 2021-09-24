# 통과했음.

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

fin = False

for l in range(N):
    for m in range(M):
        need, visited, idx_lst = [], [], []
        need.append((l, m))

        while need:
            i, j = need.pop()
            visited.append((i, j))

            cnt = 0
            for p in range(4):
                x = i + dx[p]
                y = j + dy[p]
                if x<0 or y<0 or x>=N or y>=M:
                    continue

                if (x, y)==visited[0] and len(visited)>=4:
                    fin = True
                    break

                if board[x][y]==board[i][j] and (x, y) not in visited:
                    need.append((x, y))
                    cnt += 1

            for q in range(cnt-1):
                idx_lst.append((i, j))

            if cnt==0 and need:
                k = idx_lst.pop()
                for v in range(len(visited)-1, -1, -1):
                    if visited[v] == k:
                        break
                    visited.pop()
            if fin: break
        if fin: break
    if fin: break

if fin:
    print('Yes')
else:
    print('No')


# 백준 정답
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# n,m = map(int,input().split())
# a = [input() for _ in range(n)]
# dist = [[0]*m for _ in range(n)]
# check = [[False]*m for _ in range(n)]
# def go(x, y, cnt, color):
#     if check[x][y]:
#         if cnt-dist[x][y] >= 4:
#             return True
#         else:
#             return False
#     check[x][y] = True
#     dist[x][y] = cnt
#     for k in range(4):
#         nx,ny = x+dx[k],y+dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if a[nx][ny] == color:
#                 if go(nx,ny,cnt+1,color):
#                     return True
#     return False
# for i in range(n):
#     for j in range(m):
#         if check[i][j]:
#             continue
#         dist = [[0]*m for _ in range(n)]
#         ok = go(i, j, 1, a[i][j])
#         if ok:
#             print('Yes')
#             exit()
# print('No')
