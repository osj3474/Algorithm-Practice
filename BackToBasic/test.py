# N, M, K = map(int, input().split())
# board = [input() for _ in range(N)]
# src_x, src_y, dest_x, dest_y = map(int, input().split())
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
class Node:
    def __init__(self, x, y, prev_lst):
        self.x=x
        self.y=y
        self.prev_lst=prev_lst
    def get_xy(self):
        return self.x, self.y
    def add_lst(self, ele):
        self.prev_lst.append(ele)

board=['...','#.#','...']

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# DS, BQ
# 최소니까 BQ로 해야한다.

from collections import deque
route = deque()
N, M = 3, 3
srcX, srcY, destX, destY = 0, 0, 2, 0

visited = list()
route.append(Node(srcX, srcY, [(srcX, srcY)]))
breakFlag=False

while route:
    node = route.popleft()
    i, j = node.get_xy()
    prev_lst = node.prev_lst
    print("{}, {}노드를 할꺼구, 지나온 길은 {}야.".format(i, j, node.prev_lst))
    for p in range(4):
        x = i+dx[p]
        y = j+dy[p]
        if x >= M or x < 0 or y >= N or y < 0 or ((x, y) in node.prev_lst): continue
        if board[x][y]=='.':
            if (x, y) == (destX, destY):
                node.add_lst((x, y))
                breakFlag = True; break
            print("     지금 {}, {}에서 {}리스트가 추가될거야.".format(x, y, prev_lst+[(x,y)]))
            route.append(Node(x, y, prev_lst+[(x,y)]))
    if breakFlag: break

print(node.prev_lst)

