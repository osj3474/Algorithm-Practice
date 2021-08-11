N, M = map(int, input().split())
A = [0]*(N+1)

def go(idx, n, m):
    if idx==m:
        for i in range(m):
            print(A[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if A[idx-1]>i: continue
        A[idx] = i
        go(idx+1, n, m)

go(0, N, M)