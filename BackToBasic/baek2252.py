# 위상정렬이 이런거구나.
# DAG = 단방향 no사이클인 그래프에서
# 순서를 지정하는거

from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
edge_lst = [list(map(int, input().split())) for _ in range(M)]

node_dic = defaultdict(list)
inbound_lst = [0]*(N+1)
queue = deque()
result = list()

for e in edge_lst:
    node_dic[e[0]].append(e[1])
    inbound_lst[e[1]]+=1

for i in range(1, len(inbound_lst)):
    if inbound_lst[i]==0:
        queue.append(i)

while queue:
    now = queue.popleft()
    for i in node_dic[now]:
        inbound_lst[i] -= 1
        if inbound_lst[i]==0: queue.append(i)
    result.append(now)
    node_dic[now] = []

for i in list(result):
    print(i, end=' ')