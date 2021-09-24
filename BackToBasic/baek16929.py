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
                # print('다시 갈림길로 돌아가야 해 => {}를 향해!'.format(k))
                for v in range(len(visited)-1, -1, -1):
                    if visited[v] == k:
                        break
                    visited.pop()
                # print('visited = {}'.format(visited))
            if fin: break
        if fin: break
    if fin: break

if fin:
    print('Yes')
else:
    print('No')