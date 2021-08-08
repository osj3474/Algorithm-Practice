# D[n] = n을 1,2,3의 합으로 나타낼 수 있는 경우의 수
# (연속된 수 X)
# => 마지막 수를 i라 두자. {A-i}의 원소만 가능

# D[n][1] = D[n-1][2] + D[n-1][3]
# D[n][2] = D[n-2][1] + D[n-2][3]
# D[n][3] = D[n-3][1] + D[n-3][2]

n = int(input())
num_lst = [int(input()) for _ in range(n)]
MAX = max(num_lst)
k = 1000000009
dp = [[0]*4 for _ in range(MAX+1)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, MAX+1):
    dp[i][1] = dp[i-1][2]%k+dp[i-1][3]%k
    dp[i][2] = dp[i-2][1]%k+dp[i-2][3]%k
    dp[i][3] = dp[i-3][1]%k+dp[i-3][2]%k

for i in num_lst:
    print((dp[i][1]+dp[i][2]+dp[i][3])%k)