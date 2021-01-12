# N = int(input())
# house_lst = [list(map(int, input().split())) for _ in range(N)]

N = 4
house_lst = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]

def move(house_lst, idx, cnt = 0):
    i, j = idx
    if i != 0:
        if house_lst[i - 1, j] == 0:  # up가능
            cnt += 1
            move(house_lst, i - 1, j, cnt)
    if i != N:
        if house_lst[i+1, j]:    # down 가능
            cnt += 1
            move(house_lst, i+1, j, cnt)
    if j != 0:
        if house_lst[i, j-1] == 0:    # left 가능
            cnt += 1
            move(house_lst, i, j-1, cnt)
    if j != N:
        if house_lst[i, j+1] ==0:    # right 가능
            cnt += 1
            move(house_lst, i, j+1, cnt)
