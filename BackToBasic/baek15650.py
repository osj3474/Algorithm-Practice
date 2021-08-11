N, M = map(int, input().split())
c = [False]*(N+1)
A = [0]*(N+1)

def go(idx, n, m):
    if idx==m:
        for i in range(m):
            print(A[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if c[i]==True or A[idx-1]>i:
            continue
        c[i]=True
        A[idx]=i
        go(idx+1, n, m)
        c[i]=False

go(0, N, M)