# N = int(input())
# M = int(input())
# bus_lst = [list(map(int, input().split())) for _ in range(M)]
# S, T = map(int, input().split())
#
# edge_dic = dict()
# for i in range(1, N+1):
#     edge_dic[i]=dict()
#
# for bus in bus_lst:
#     start, end, price = bus[0], bus[1], bus[2]
#     edge_dic[start].update({end:price})
#
# print(edge_dic)


N = int(input())
M = int(input())
bus_lst = [list(map(int, input().split())) for _ in range(M)]
s, t = map(lambda x:int(x)-1, input().split())


inf = float('inf')
board = [[-1]*N for _ in range(N)]

for bus in bus_lst:
    board[bus[0]-1][bus[1]-1] = bus[2]

for i in range(N):
    for j in range(N):
        if i==j: board[i][j]=0; continue
        if board[i][j]==-1: board[i][j]=inf



# board = [
#     [0, 2, 5, 1, inf, inf],
#     [2, 0, 3, 2, inf, inf],
#     [5, 3, 0, 3, 1, 5],
#     [1, 2, 3, 0, 1, inf],
#     [inf, inf, 1, 1, 0, 2],
#     [inf, inf, 5, inf, 2, 0]
# ]
v = [False]*N
d = [0]*N

def getSmallIndex():
    min = float('inf')
    idx = 0
    for i in range(N):
        if d[i]<min and not v[i]:
            min = d[i]
            idx = i
    return idx

for i in range(N):
    d[i] = board[s][i]
v[s] = True
for i in range(N-2):
    cur = getSmallIndex()
    v[cur] = True
    for j in range(N):
        if not v[j]:
            if d[cur]+board[cur][j] < d[j]:
                d[j] = d[cur]+board[cur][j]

print(d[t])

