def Find(v, parent):
    if parent[v] != v:
        parent[v] = Find(parent[v], parent)
    return parent[v]

def Union(u, v, parent, rank):
    x, y = Find(u, parent), Find(v, parent)
    if x==y: return
    if rank[x] > rank[y]:
        parent[y]=x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y]=x
        rank[x]+=1
    return parent, rank