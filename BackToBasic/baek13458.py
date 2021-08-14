N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N
for i in range(N):
    A[i] -= B
    if A[i]<=0: continue
    cnt += A[i] // C
    if A[i]%C!=0: cnt += 1

print(cnt)