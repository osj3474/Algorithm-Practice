MAX = 10000

N = MAX-1
for n in str(N):
    N += int(n)

d = [0]*(N+1)
for i in range(MAX):
    idx = i
    for n in str(i):
        idx += int(n)
    d[idx] = 1

for i in range(1, MAX):
    if d[i] == 0:
        print(i)