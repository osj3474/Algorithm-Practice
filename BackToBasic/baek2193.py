# n = int(input())
# d = [0]*91
# d[1] = 1
# d[2] = 1
#
# for i in range(3, n+1):
#     d[i]= d[i-1] + d[i-2]
#
# print(d[n])

N = int(input())
dp = [[0]*2 for _ in range(N+1)]
dp[1][0], dp[1][1] = 1, 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[N])-dp[N][0])