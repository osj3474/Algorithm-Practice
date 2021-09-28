from collections import deque

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

# 같은 거리에 있는 것 중에 위 > 왼 순으로 먹어야 하기 때문에
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 아기 상어가 큰 상어들 사이에 둘러쌓여서 못 나갈 수도 있기 때문에
# 2중 for문으로 보드판을 보면서 남은 물고기를 확인하는 방식은 부적합
age, level = 2, 2

# 첫 위치
i, j = 0, 0
fin = False
for i in range(N):
    for j in range(N):
        if a[i][j]==9:
            a[i][j] = 0
            fin = True
            break
    if fin: break

need, new_lst, visited = deque(), list(), list()
need.append((i, j))


answer, cnt = 0, 1
limit = 30
while need:
    limit -= 1
    i, j = need.popleft()
    visited.append((i, j))

    for p in range(4):
        x = i + dx[p]
        y = j + dy[p]

        if 0<=x<N and 0<=y<N and a[x][y]<=age and (x, y) not in visited and (x, y) not in new_lst:
            if 0<a[x][y]<age:
                level -= 1
                if level == 0:
                    age += 1
                    level = age
                a[x][y] = 0
                new_lst.clear()
                visited.clear()
                need.clear()
                answer += cnt
                cnt = 1

                need.append((x, y))

                break
            new_lst.append((x, y))

    if not need:
        need.extend(new_lst)
        new_lst.clear()
        cnt += 1

print(answer)