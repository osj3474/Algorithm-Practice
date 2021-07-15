N, M = map(int, input().split())
board = [list(map(lambda x:int(x), input())) for _ in range(N)]

from collections import deque
from copy import deepcopy

class Node:
    def __init__(self, x, y, cnt):
        self.x = x
        self.y = y
        self.prev = set()
        self.cnt = cnt
    def getInfo(self):
        return self.x, self.y, self.prev, self.cnt

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

need = deque()
need.append(Node(0, 0, 1))
destX, destY = N-1, M-1
check_lst = [[0]*M for _ in range(N)]

while need:
    node = need.popleft()
    i, j, prev, cnt = node.getInfo()
    prev_length = len(prev)
    if check_lst[i][j] != 0 and check_lst[i][j] < prev_length: continue
    print('[{}] {}, {}를 하고, prev={}, cnt={}입니다.'.format(cnt, i, j, prev, cnt))
    if (i, j)==(destX, destY):
        print("종료되었습니다.")
        break
    if board[i][j]==0:
        print('   {}, {}는 0이라 못가요.'.format(i, j))
        continue
    for p in range(4):
        x=i+dx[p]
        y=j+dy[p]
        if x>=N or y>=M or x<0 or y<0 or (x, y) in prev: continue
        if board[x][y]!=0:
            temp = deepcopy(prev)
            temp.add((i, j))
            print('       다음 스텝으로 {}, {}를 넣습니다. 직전 친구는 {}입니다.'.format(x, y, temp))
            new = Node(x, y, cnt + 1)
            new.prev = temp
            check_lst[x][y]=len(temp)
            print('       그리고 check[{}][{}]리스트에는 {}가 들어갔습니다.'.format(x, y, check_lst[x][y]))
            need.append(new)

print(check_lst)
print(cnt)

# 2178