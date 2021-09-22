N, M = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(N):
    total = 0
    for j in range(i, N):
        total += a[j]
        if total==M:
            cnt += 1

print(cnt)