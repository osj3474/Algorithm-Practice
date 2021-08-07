# T = int(input())
# n_lst = [int(input()) for _ in range(T)]

# 작은 문제로 나눌 수 있다. => 점화식
# 한 문제의 정답은 하나이다. =>

def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n>=2:
        dp[2] = 2
        if n == 2: return dp[2]
    if n>=3:
        dp[3] = 4
        if n == 3: return dp[3]
        for i in range(4, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]

n = int(input())
for _ in range(n):
    print(solution(int(input())))