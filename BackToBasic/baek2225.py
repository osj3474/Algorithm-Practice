# dp[k][n] = sum(dp[k-1][N-L]) // 0<=L<=N
# 지금 찾을 때, N을 K개로 만드는데, 0을 0개로 만드는 것부터 N을 K개로 만드는 경우 전부를 구할거임.
# (혼자 문제를 풀때는, 이 부분에서 막힌거 같다.)
# dp[0][0]을 1로 해줘야 0을 사용하는 경우의 수를 카운트 할 수 있다.
# mod를 할 때는, dp에 넣을 때부터 mod를 해줘서 수가 너무 커서 출력초과가 되지 않게 하자.

N, K = map(int, input().split())
answer = 0
mod = 1000000000
dp = [[0]*201 for _ in range(201)]
dp[0][0] = 1
for i in range(1, K+1):
    for j in range(N+1):
        for l in range(j+1):
            dp[i][j] += dp[i-1][j-l]
        dp[i][j] %= mod

print(dp[K][N])