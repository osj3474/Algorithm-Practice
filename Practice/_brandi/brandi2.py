# 4
# 3 4
# 2 3
# 2 1
# 4 1
# 5
# 1 2
# 2 4
# 3 1
# 4 1
# 1 2

# input
N = int(input())
light_dic = {}
adjacent_dic = {}

def appendRoutes(routes_dict, key, value):
    try:
        routes_dict[key].append(value)
    except:
        routes_dict[key] = [value]
    return routes_dict

for i in range(N):
    key = sorted(list(map(int, input().split())))
    key_str = str(key[0])+' '+str(key[1])
    light_dic[key_str] = 0
    one, other = key
    adjacent_dic = appendRoutes(adjacent_dic, one, other)
    adjacent_dic = appendRoutes(adjacent_dic, other, one)

M = int(input())
path_lst = [list(map(int, input().split())) for _ in range(M)]


def movePath(adjacent_dic, start, dest):
    ret = []
    if dest in adjacent_dic[start]:
        ret.append([start, dest])
    else:
        next = min(adjacent_dic[start])
        ret.append([start, next])
        return ret + movePath(adjacent_dic, next, dest)
    return ret

def toggleLight(light_dic, move_lst):
    for node in move_lst:
        node.sort()
        key = str(node[0]) + ' ' + str(node[1])
        if light_dic[key] == 0:
            light_dic[key] = 1
        else:
            light_dic[key] = 0
    return light_dic

def Find(x, parent):
    # print('이번에 부모를 찾는 노드는 {}입니다.'.format(x))
    # print('현재 parent입니다. --> ', parent)
    if parent[x] == x:
        return parent[x]
    else:
        return Find(parent[x], parent)

def Union(x, y, parent, rank):
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

def makeParentRank(adjacent_dic):
    parent = {}
    rank = {}
    for key, value in adjacent_dic.items():
        parent[key] = key
        rank[key] = 0
    return parent, rank

for path in path_lst:
    parent, rank = makeParentRank(adjacent_dic)
    move_lst = movePath(adjacent_dic, path[0], path[1])
    light_dic = toggleLight(light_dic, move_lst)
    for key, value in light_dic.items():
        if value == 1:
            one, other = map(int, key.split())
            # print('{}들고 Find 진입'.format(one))
            p1 = Find(one, parent)
            # print('Find 끝')
            # print('{}들고 Find 진입'.format(other))
            p2 = Find(other, parent)
            # print('Find 끝')
            if Find(one, parent) != Find(other, parent):
                Union(p1, p2, parent, rank)
    # print(light_dic)
    node_set = set()
    for value in parent.values():
        node_set.add(value)
    print(len(node_set))



