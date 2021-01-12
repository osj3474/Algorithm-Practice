## 반례를 찾아보자!!!
# 대표 반례 [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,1,0,1]] 이 반례를 기억하자..!
n = int(input())
List = []
for i in range(n) :
    List.append([int(x) for x in input().split()])
def Find(v, parent) : 
    if parent[v] != v : parent[v] = Find(parent[v], parent)
    return parent[v]
def Union(x, y, parent, rank) : 
    if rank[x] > rank[y] : 
        parent[y] = x
    elif rank[x] < rank[y] : 
        parent[x] = y
    else : 
        parent[y] = x
        rank[x] += 1
    return parent, rank
def solution(n, computers):
    parent = {}
    rank = {}
    for i in range(n) :
        parent[i] = i
        rank[i] = 0
    ## 고유 인덱스가 저장이 되지 않는다! 이거 명심하자!
    for i in range(len(computers)) : 
        for edge in range(len(computers[i])) : 
            if edge == i : 
                continue
            if computers[i][edge] == 1 : 
                v1 = i
                v2 = edge
                x = Find(v1, parent)
                y = Find(v2, parent)
                if x != y :
                    parent, rank = Union(x, y, parent, rank)
    # 추가적으로 최종 부모값을 갱신하는 과정 need
    for i in range(n) :
        root = Find(i, parent)
        parent[i] = root
                
    value = []
    value = list(parent.values())
    value_set = len(set(value))
    print(value)
    #answer = 1
    #get = [value[0]]
    #for i in range(1, len(value)):
    #    if value[i] not in get :
    #        answer += 1
    #        get.append(value[i])
    return value_set

def main():
    n = 5
    computers = [[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,0],[0,1,0,1,1],[1,0,0,1,1]]
    print(solution(n, computers))


print(solution(n, List))


