def search(graph, start):
    need, visited = list(), list()
    need.append(start)
    while need:
        node = need.pop(0)
        if node not in visited:
            visited.append(node)
            need.extend(graph[node])
    for visit in visited:
        del graph[visit]
    return graph

def solution(n, computers):
    graph = {}
    i = 0
    for computer in computers:
        graph[i] = [j for j in range(n) if computer[j] == 1 and j != i]
        i+=1
    cnt = 0
    while graph:
        cnt += 1
        graph = search(graph, list(graph.keys())[0])
    return cnt
