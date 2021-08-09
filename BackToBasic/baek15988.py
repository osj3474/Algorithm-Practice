n = int(input())
lst = [int(input()) for _ in range(n)]
mod = 1000000009

M = max(lst)
dp = [0]*(M+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, M+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod

for i in lst:
    print(dp[i])