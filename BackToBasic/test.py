# from collections import defaultdict
#
# def bfs(here, visited, graph):
#
#     if visited[here]:
#         print(visited[here])
#         if visited[here] == -1:
#             print("??")
#             return True
#         return False
#
#     visited[here] = -1
#     for node in graph[here]:
#         if bfs(node, visited, graph):
#             return True
#     visited[here] = 1
#     return False
#
# def solution():
#     N=7
#     edges = [(1,2), (1, 5), (2, 3), (2, 6), (3, 4), (6, 4), (4, 7), (7, 6)]
#
#     graph = defaultdict(list)
#     for edge in edges:
#         v, w = edge
#         graph[v].append(w)
#
#     visited = [0]*(N+1)
#     return bfs(2, visited, graph)
#
# print(solution())

if(-1):print(1)