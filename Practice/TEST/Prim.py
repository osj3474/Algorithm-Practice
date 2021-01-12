from collections import defaultdict
from heapq import *

def prim(start_node, edges) :
    mst = []
    adjacent_edges = defaultdict(list)
    for n1,n2,weight in edges :
        adjacent_edges[n1].append([weight,n1,n2])
        adjacent_edges[n2].append([weight,n2,n1])
    connected_nodes = [start_node]
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)
    minimum_weight = 0
    while candidate_edge_list :
        weight,n1,n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes :
            connected_nodes.append(n2)
            mst.append([weight,n1,n2])
            minimum_weight += weight
            for edge in adjacent_edges[n2] :
                if edge[2] not in connected_nodes :
                    heappush(candidate_edge_list, edge)

    return mst, minimum_weight





graph = [[0,1,5], [0,3,2], [0,4,3], [1,4,1], [3,4,10],[1,2,2],[2,5,3],[4,5,4]]

mst, minimum_weight = prim(0, graph)
print(mst)
print(minimum_weight)
