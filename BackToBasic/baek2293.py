import sys

n, k = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(n)]

d = [0]*(k+1)
d[0] = 1
length = len(A)

for j in range(length):
    for i in range(k+1):
        if i<A[j]: continue
        d[i] += d[i-A[j]]

print(d[k])