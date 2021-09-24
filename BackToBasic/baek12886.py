# 다시 풀어볼 문제~!!

# from collections import deque   # 첫번째 시도
#
# def solution(a):
#     if sum(a)%3 != 0:
#         return 0
#
#     need, visited = deque(), list()
#     need.append(a)
#
#     limit = 20
#
#     while need and limit:
#         limit -= 1
#         now = need.popleft()
#         if now[0] == now[1] and now[1] == now[2]:
#             return 1
#
#         now.sort()
#
#         visited.append(now)
#
#         for i, j, k in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
#             x, y, z = now[i], now[j], now[k]
#
#             temp = x
#
#             x += temp
#             y -= temp
#
#             sorted_lst = sorted([x, y, z])
#
#             if 0<=x<=1000 and 0<=y<=1000 and 0<=z<=1000 and sorted_lst not in visited:
#                 need.append(sorted_lst)
#
#     return 0
#
# a = list(map(int, input().split()))
# print(solution(a))

import sys
sys.setrecursionlimit(1500*1500)
check = [[False]*1501 for _ in range(1501)] # 3개의 그룹이지만, 2차원 배열로 할 수 있는 이유는
x,y,z = map(int,input().split())

s = x+y+z     # key point

def go(x, y):
    if check[x][y]:
        return
    check[x][y] = True
    a = [x, y, s-x-y]       # 총합은 바뀌지 않는다는 사실을 이용하여 한 요소를 줄였기 때문,,,!
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]: # 가능한 경우의 수 중에서 x, y
                b = [x, y, s-x-y]
                b[i] += a[i]
                b[j] -= a[i]
                go(b[0], b[1])
if s % 3 != 0:
    print(0)
else:
    go(x,y)
    if check[s//3][s//3]: # 두 그룹의 값이 모두 s//3 인 경우 => 나머지 한 값도 s//3 임. (총합은 s니까)
        print(1)
    else:
        print(0)