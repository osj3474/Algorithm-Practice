N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

length = 1
past = [A[0][0]]
for i in range(1, N):
    size = length*2
    past = new
    new = [0]*size
    for p in past:
        new[0] = past[p]+A[i][0]
        new[-1] = p+A[i][-1]
        k = 1
        for j in range(1, size-2, 2):
            new[j] = p+A[i][k]
            new[j+1] = p+A[i][k]
