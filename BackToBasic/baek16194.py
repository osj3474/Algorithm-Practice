N = int(input())
p_lst = [0]+list(map(int, input().split()))

dp = [0]*(N+1)
dp[1] = p_lst[1]
for i in range(2, N+1):
    dp[i] = min([dp[i-j]+p_lst[j] for j in range(1, i)]+[p_lst[i]])

print(dp[N])