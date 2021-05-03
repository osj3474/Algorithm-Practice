N = int(input())
A = list(map(int, input().split()))
d = [1] * N
MAX = 0

for i in range(N):
    temp = 0
    for j in range(i):
        if A[i] > A[j] and temp < d[j]:
            temp = d[j]
    d[i] += temp
    if MAX < d[i]: MAX = d[i]

print(MAX)