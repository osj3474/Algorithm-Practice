def Find(v, parent) :
    if parent[v] != v:
        parent[v] = Find(parent[v], parent)
    return parent[v]

def Union(u, v, parent, rank) :
    x, y = Find(u), Find(v)
    if x==y: return
    if rank[x] > rank[y]:
        parent[y]=x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y]=x
        rank[x]+=1

parent, rank = dict(), dict()
for i in range(N*M):
    parent[i]=i
    rank[i]=0