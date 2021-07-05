from collections import defaultdict

N, M, K = map(int, input().split())
point_lst = [list(map(int, input().split())) for _ in range(K)]
board = [[0]*(M+1) for _ in range(N+1)]
parent = [[0]*(M+1) for _ in range(N+1)]
p = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for x, y in point_lst:
    board[x][y] = 1

# for i in range(len(board)):
#     print(board[i])

cnt = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        temp = []
        temp.append([i, j])
        print("{}, {} 될까?".format(i, j))
        while temp:
            cnt += 1
            if cnt > 30: exit()
            X, Y = temp.pop()
            if board[X][Y]!=1: continue
            print("   {}, {} 지점합니다.".format(X, Y))
            for k in range(4):
                x = X+dx[k]
                y = Y+dy[k]
                if x < 1 or x >= N+1 or y < 1 or y >= N+1: continue
                print("        {}, {} 탐색중.".format(x, y))
                if parent[x][y]!=0:
                    parent[i][j]=parent[x][y]
                    print("               {}, {}의 parent에 {}를 할당합니다.".format(i, j, parent[x][y]))
                if board[x][y]==1 and parent[x][y]==0:
                    temp.append([x, y])
                    print("               temp에 {}, {}를 추가합니다.".format(x, y))
                    print("               temp = {}".format(temp))
            if parent[X][Y]==0:
                if temp==[]: p += 1
                print("                ------- parent 증가합니다 ---------")
                parent[X][Y]=p


temp_dict = defaultdict(int)
for i in range(1, N+1):
    for j in range(1, M+1):
        temp_dict[parent[i][j]]+=1

print(parent)
print(temp_dict)
print(max(temp_dict.values()))

# for i in range(N):
#     for j in range(M):
#         x = point_lst
#
#
#
# # 지금 보드에 0, 1로 아예 표시가 된 녀석을 쓰는 것도 아닌데, 왜 판을 만든 상황을 가정하고 진행할 필요가 없지 않은가.
#
# # [[3, 2], [2, 2], [3, 1], [2, 3], [1, 1]]
# pocket_lst = list()
# for i in range(K):
#     print(point_lst[i])
#     # pocket_lst.append(set(point_lst[i]))
#
# print(pocket_lst)
# pocket_lst[0].add([2])
#
#
#
# visited_lst = [1]*K
# for i in range(K-1):
#     for j in range(i+1, K):
#         x = point_lst[i][0]
#         y = point_lst[i][1]
#         for p in range(4):
#             if point_lst[j]==[x+dx[p], y+dy[p]]:
#                 print(type(pocket_lst[i]))
#                 # pocket_lst[i].add(point_lst[i])
#                 # pocket_lst[j].add(point_lst[j])
#                 # break
#         print(pocket_lst)
#
#
# print(max(visited_lst))




# # 셀 마스터
# class NodeMgmt:
#     def __init__(self, x):
#         self.x = x
#
# # 셀 하나
# class Node:
#     def __init__(self, x:int , y:int):
#         self.x = x
#         self.y = y
#         self.parent = None
#     def setParent(self, p):
#         self.parent = p
#     def getParent(self):
#         return self.parent
#
# # 시계 방향으로 돈다
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# # 2중 for문 안에 x, y를 재정의한다. (by dx, dy)
# for i in range(N):
#     for j in range(M):
#         for p in range(4):
#             x = i+dx[p]
#             y = j+dy[p]
#             Node(x, y)
#
#
#
