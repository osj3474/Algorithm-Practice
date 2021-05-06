N = int(input())
d = [[10] + [1 for _ in range(10)]]
d += [[0]*11 for _ in range(N-1)]

for i in range(1, N):
    d[i][0] = d[i][1] = d[i-1][0]
    for j in range(2, 11):
        d[i][j] = d[i][j-1]-d[i-1][j-1]
        d[i][0] += d[i][j]

print(d[N-1][0] % 10007)