def search(graph, start):
    need, visited = list(), list()
    need.append(start)
    while need:
        node = need.pop(0)
        if node not in visited:
            visited.append(node)
            need.extend(graph[node])
    return visited

N, M = map(int, input().split())
node_lst = [list(map(int, input().split())) for _ in range(M)]
graph = {}
for i in range(1,N+1):
    graph[i] = []

for node in node_lst:
    graph[node[0]].append(node[1])

answer = 0
if len(search(graph, list(graph.keys())[0])) != N:
    answer = 'bug'

def checkCycle(temp, new, total):
    total += new[2]
    new[1]
    return total
for i in range(N):
    temp = node[:]
    total = 0
    while 1:
        try:
            new = temp.pop(i)
            total += checkCycle(temp, new, total)
        except:
            break



