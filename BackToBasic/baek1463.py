from collections import defaultdict
# 왜 DP 인가?
# 조건1: 작은 문제로 쪼갤 수 있다.   => 점화식
# 조건2: 한 문제의 정답은 같아야한다. => memo를 쓸 수 있다.

# 점화식 => D[N]=min(D[N-1], D[N//2], D[N//3])+1
# 구현   => 재귀

# def operate(n, memo):  # return: 최솟값
#     # base
#     if n==1:
#         return 0
#     # memorization
#     if memo[n] > 0:
#         return memo[n]
#
#     # recursive
#     memo[n] = operate(n-1, memo)+1
#     if n%2==0:
#         temp = operate(n//2, memo)+1
#         memo[n] = min(memo[n], temp)
#     if n%3==0:
#         temp = operate(n//3, memo)+1
#         memo[n] = min(memo[n], temp)
#     return memo[n]
#
# n = int(input())
# memo = [0]*(n+1)
# print(operate(n, memo))


N = int(input())
dp = [0]*(N+1)
dp[1] = 0

for i in range(2, N+1):
    lst = []
    if i%3==0: lst.append(dp[i//3])
    if i%2==0: lst.append(dp[i//2])
    lst.append(dp[i-1])
    dp[i]=min(lst)+1

print(dp[N])