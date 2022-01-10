N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 세팅 >> '.'=0 / '*'=1
ck = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == '*':
            ck[i][j] = 1

# for i in ck:
#     print(i)

limit = min(N, M)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# (x, y)에서 그릴 수 있는 십자가의 크기를 리스트로 반환하는 함수
def find_cross(x:int, y:int) -> list:
    if board[x][y] == '.':
        return []


    ret = []
    fin = False
    for i in range(1, limit+1):  # 십자가의 크기 배율 : 1~limit
        for j in range(4):       # 상, 하, 좌, 우
            cx = x+dx[j]*i
            cy = y+dy[j]*i

            # print('({}, {}) 확인 시작'.format(cx, cy))
            if cx<0 or cx>=N or cy<0 or cy>=M:
                fin = True
                break

            if board[cx][cy]=='*':
                continue
            # print('     ({},{}) 에서 fail 됨.'.format(cx, cy))
            fin = True; break    # break point
        if fin: break

        ret.append(i)            # 십자가를 만들수 있는 경우
        ck[x][y] = 0  # 만들어낸 것.
        for j in range(4):
            cx = x + dx[j] * i
            cy = y + dy[j] * i
            ck[cx][cy] = 0

    return ret

cnt = 0
answer = []
for i in range(1, N-1):
    for j in range(1, M-1):
        num_lst = find_cross(i, j)
        # print('({},{}) ===> {}'.format(i, j, num_lst))
        if num_lst:
            for num in num_lst:
                answer.append([i, j, num])
                cnt += 1

flag = False
for i in range(N):
    for j in range(M):
        if ck[i][j] == 1:
            flag = True
            break
        if flag:
            break

if flag:
    print(-1)
else:
    print(cnt)
    for x, y, n in answer:
        print(x+1, y+1, n)

# for i in ck:
#     print(i)

# print()
# print(answer)