N = int(input())
S = list(map(int, input().split()))

c = [False]*10000001

def go(idx, total):
    if idx==N: return
    c[total] = True
    go(idx + 1, total)

    total += S[idx]
    c[total] = True
    go(idx+1, total)


for i in range(N):
    go(i, 0)

for i in range(1, len(c)):
    if c[i]==False:
        print(i)
        break