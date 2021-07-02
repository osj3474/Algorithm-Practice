N, M, K = map(int, input().split())
point_lst = [list(map(int, input().split())) for _ in range(K)]

# 지금 보드에 0, 1로 아예 표시가 된 녀석을 쓰는 것도 아닌데, 왜 판을 만든 상황을 가정하고 진행할 필요가 없지 않은가.

# [[3, 2], [2, 2], [3, 1], [2, 3], [1, 1]]
pocket_lst = list()
for i in range(K):
    print(point_lst[i])
    # pocket_lst.append(set(point_lst[i]))

print(pocket_lst)
pocket_lst[0].add([2])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited_lst = [1]*K
for i in range(K-1):
    for j in range(i+1, K):
        x = point_lst[i][0]
        y = point_lst[i][1]
        for p in range(4):
            if point_lst[j]==[x+dx[p], y+dy[p]]:
                print(type(pocket_lst[i]))
                # pocket_lst[i].add(point_lst[i])
                # pocket_lst[j].add(point_lst[j])
                # break
        print(pocket_lst)


print(max(visited_lst))




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
