# 백트래킹
N, M = map(int, input().split())

# 보드 및 coin위치 세팅
BOARD = list()
coin_lst = list()
for i in range(N):
    line = input()
    temp = list()
    for j in range(M):
        if line[j] == "o":
            coin_lst.append([i, j])
        temp.append(line[j])
    BOARD.append(temp)


# 이동시 1) 둘다 동시에 범위를 벗어나면 stop 2)10이상이면 out
def move(coin_lst:list, cnt:int):
    print(coin_lst, cnt)
    # 1)
    flag = 0
    for i in range(2):
        x, y = coin_lst[i]
        if x<0 or x>=N or y<0 or y>=M:
            flag += 1
    if flag == 2:
        return -1

    # 2)
    if cnt > 10:
        return -1
    print("flag=", flag)
    # base case
    if flag == 1:
        return cnt

    cnt += 1
    # 상, 하, 좌, 우 모두 움직이는 재귀
    x1, y1, x2, y2 =coin_lst[0][0], coin_lst[0][1], coin_lst[1][0], coin_lst[1][1]
    print(x1-1)
    print(y1)

    # 그런 다음에 . 인지 # 인지에 따라서 이동한다.
    if BOARD[x1-1][y1] == "#":
        x1 -= 1
    if BOARD[x2-1][y2] == "#":
        x2 -= 1
    move([[x1, y1], [x2, y2]], cnt)

    if BOARD[x1+1][y1] == "#":
        x1 += 1
    if BOARD[x2+1][y2] == "#":
        x2 += 1
    move([[x1, y1], [x2, y2]], cnt)

    if BOARD[x1][y1-1] == "#":
        y1 -= 1
    if BOARD[x2][y2-1] == "#":
        y2 -= 1
    move([[x1, y1], [x2, y2]], cnt)

    if BOARD[x1][y1+1] == "#":
        y1 += 1
    if BOARD[x2][y2+1] == "#":
        y2 += 1
    move([[x1, y1], [x2, y2]], cnt)



answer_lst = []
print(" BOARD ")
for i in range(N):
    print(BOARD[i])
print("coin_lst:", coin_lst)
print("N:", N, "M:", M)
print(move(coin_lst, 0))

# challenge
# BOARD 업데이트, 최소값을 알아내야하는데, 그부분을 어디에 추가해야하는지 잘 모르겟음.