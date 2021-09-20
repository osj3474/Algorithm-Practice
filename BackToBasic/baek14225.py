N = int(input())
a = list(map(int, input().split()))

c = [False]*100001

def go(i, total):
    if i>=N: return

    c[total] = True
    go(i+1, total)

    total += a[i]
    c[total] = True
    go(i+1, total)

for i in range(N):
    go(i, 0)

for i in range(1, 100001):
    if not c[i]: break

print(i)