n = int(input())
xy_lst = [list(map(int, input().split())) for _ in range(n)]

entire = [[0 for _ in range(100)] for _ in range(100)]
def ck(lst):
    for i in range(lst[0], lst[0]+10):
        for j in range(lst[1], lst[1]+10):
            entire[i][j] = 1

for i in range(n):
    ck(xy_lst[i])

total = 0
for i in range(100):
    total += entire[i].count(1)
print(total)
