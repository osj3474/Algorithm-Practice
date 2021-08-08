# dp[n]=n을 제곱수로 나타낼때 최소항의 갯수
# =min(dp[n-i*i])+1
N = int(input())
dp = [0]*(N+1)

for i in range(1, N+1):
    dp[i]=i        # 초기화는 자기자신 = 1^2의 합인 경우
    j = 1
    while i-j*j>=0:
        value = dp[i-j*j]+1
        if dp[i] > value: dp[i] = value
        j += 1

print(dp[N])