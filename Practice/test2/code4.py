import copy
import sys
sys.setrecursionlimit(1000000)

def throwStone(stream, i, j, total, limit):
    print("인덱스:", i, j)
    if limit == 0:
        return total
    if i != 0:
        if stream[i - 1][j] == 0:  # up가능
            total += 1
            stream[i - 1][j] = 1
            throwStone(stream, i - 1, j, total,limit-1)
    if i != N-1:
        if stream[i+1][j] == 0:    # down 가능
            total += 1
            stream[i + 1][j] = 1
            print("here")
            print(i+1, j)
            for st in stream:
                print(st)
            print("")
            throwStone(stream, i+1, j, total,limit-1)
    if j != 0:
        if stream[i][j-1] == 0:    # left 가능
            total += 1
            stream[i][j - 1] = 1
            throwStone(stream, i, j-1, total,limit-1)
    if j != N-1:
        if stream[i][j+1] ==0:    # right 가능
            total += 1
            stream[i][j + 1] = 1
            throwStone(stream, i, j+1, total,limit-1)

N, d = map(int, input().split())
stream_lst = [list(map(int, input().split())) for _ in range(N)]

MAX = 0
# for i in range(N):
#     for j in range(N):
#         if stream_lst[i][j] == 1:
#             continue
#         global stream
#         global total
#         stream = copy.deepcopy(stream_lst)
#         total = 0
#         throwStone(i, j, d)
#
#         MAX = max(MAX, total)
stream = copy.deepcopy(stream_lst)
global total
total = 0
throwStone(stream, 2, 2, d)
for st in stream:
    print(st)

MAX = max(MAX, total)
print(MAX)