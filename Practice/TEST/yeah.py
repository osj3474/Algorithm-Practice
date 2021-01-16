from itertools import combinations as cm
from collections import deque

N, M, D = map(int, input().split())
global BOARD, MAX
BOARD = deque(list(map(int, input().split())) for _ in range(N))  # 주어진 판
MAX = 0  # 최대 공격 수
position_lst = list(cm(list(range(M)), 3))   # 궁수가 위치할 수 있는 경우의 수

# 궁수들의 공격 (한 턴)
def attack(archer_lst, D):   # param: (활이 남은 궁수, 사정거리)
    global BOARD, MAX
    # 1차 공격은 그냥 바로 위만 확인
    if archer_lst[0] == N:
        for i in range(len(archer_lst)):
            x, y = archer_lst[i]
            x -= 1
            if BOARD[x][y] == 1:  # 활을 사용한 것
                BOARD[x][y] = 0
                archer_lst.remove(i)
            archer_lst[i] = x, y

    D-=1  # 사정거리 1감소
    if D==0 or not archer_lst:  # 활을 더 길게 못 쏘거나, 궁수들이 활을 다 쓴 경우 out
        return

    # 좌, 우, 상에 대해 공격
    for archer in archer_lst:
        x, y = archer
        _attack([x-1, y], D) # 좌
        _attack([x+1, y], D) # 우
        _attack([x, y+1], D) # 상

# 궁수의 공격
def _attack(archer, D):
    global BOARD
    x, y = archer
    # BOARD를 벗어나는 경우
    if x == 0 or y == 0 or x == M - 1 or y == N - 1:
        pass
    else:
        if BOARD[x][y] == 1:
            BOARD[x][y] = 0
        else:
            D -= 1  # 사정거리 1감소
            attack(archer, D)


# 궁수의 모든 배치 경우의 수에 대해 loop
for position in position_lst:
    archer_lst = list(zip([N]*M, position))  # 궁수의 초기 위치

    for i in range(N):   # 총 N라운드
        attack(archer_lst, D)  # 해당 라운드 공격

        # 한 칸 아래로 이동
        BOARD.appendleft([0]*M)
        BOARD.pop()



