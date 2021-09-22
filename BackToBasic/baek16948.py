# from collections import deque
#
# N = int(input())
# r1, c1, r2, c2 = map(int, input().split())
#
#
# dx = [-2, -2, 0, 0, 2, 2]
# dy = [-1, 1, -2, 2, -1, 1]
#
# need, visited, new = deque(), set(), list()
# need.append((r1, c1))
#
# cnt = 0
# fin = False
#
# while need:
#     i, j = need.popleft()
#     # print("[집중] {},{} 꺼냈어요!!!".format(i, j))
#     # print("[판결 전] visited: {}".format(visited))
#     # print("[판결 전] new: {}".format(new))
#     if (i, j) == (r2, c2):
#         fin = True
#         break
#
#     if (i, j) in visited:
#         continue
#
#     visited.add((i, j))
#
#     for p in range(6):
#         x = i + dx[p]
#         y = j + dy[p]
#         if x<0 or y<0 or x>=N or y>=N:
#             continue
#         if (x, y) in visited:
#             continue
#         # print('   ', x, y, "들어감")
#         new.append((x, y))
#
#
#     # print("new:", new)
#
#     if not need:
#         if not new: break
#         need = deque(new)
#         new = []
#         for n in new:
#             need.append(n)
#             visited.add(n)
#         cnt += 1
#
# if fin:
#     print(cnt)
# else:
#     print(-1)




from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dist = [[-1]*200 for _ in range(200)]
dist[r1][c1] = 0
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

need = deque()
need.append((r1, c1))

while need:
    i, j = need.popleft()

    for p in range(6):
        x = i + dx[p]
        y = j + dy[p]
        if x<0 or y<0 or x>=N or y>=N:
            continue
        if dist[x][y] == -1:
            need.append((x, y))
            dist[x][y] = dist[i][j] + 1

print(dist[r2][c2])