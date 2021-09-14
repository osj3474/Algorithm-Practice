def fibo_recur(n):       # O(2^n)
    if n<=0: return 0
    if n<=2: return 1
    return fibo_recur(n-1)+fibo_recur(n-2)


def fibo_dp(n):       # O(n)
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]


def fibo_for(n):       # O(n)
    if n<=0: return 0
    n1, n2 = 0, 1
    for i in range(n-1):
        n1, n2 = n2, n1+n2
    return n2



print(fibo_recur(4))
print(fibo_dp(4))
print(fibo_for(4))