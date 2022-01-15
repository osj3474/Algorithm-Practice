from collections import deque

N = int(input())
scv = list(map(int, input().split()))

d1 = [[9]]
d2 = [[9, 3], [3, 9]]
d3 = [[9, 3, 1], [9, 1, 3], [3, 9, 1],
      [3, 1, 9], [1, 9, 3], [1, 3, 9]]


damages = [0, d1, d2, d3]

need, visited = deque(), set()
need.append([scv, 0])

while need:
    A, cnt = need.popleft()

    # print(A, cnt)

    n = len(A)
    if n==0:
        break

    for damage in damages[n]:
        new_lst = []
        for i in range(n):
            temp = A[i]-damage[i]
            if temp<=0:
                continue
            new_lst.append(temp)
        if tuple(new_lst) not in visited:
            visited.add(tuple(new_lst))
            need.append([new_lst, cnt + 1])

print(cnt)