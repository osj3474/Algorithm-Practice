N = int(input())
d = [[]*2 for _ in range(41)]
d[0] = [1, 0]
d[1] = [0, 1]
d[2] = [1, 1]
for i in range(3, 41):
    d[i] = [d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1]]

for i in range(N):
    n = int(input())
    print(d[n][0], d[n][1])