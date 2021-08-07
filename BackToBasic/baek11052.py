N = int(input())
card_lst = [0]+list(map(int, input().split()))


# D[n] = N개를 갖기위해 지불해야하는 금액의 최댓값

memo = [0]*(N+1)
for i in range(1, N+1):
    for j in range(1, i+1):
        memo[i] = max(memo[i], memo[i-j]+card_lst[j])

print(memo[N])



# 다시 풀기
# dp[n] = n개 카드 구매 최대 비용
# = max(dp[n-1]+p[1], dp[n-2]+p[2], ...)
#
# N = int(input())
# p_lst = [0]+list(map(int, input().split()))
#
# dp = [0]*(N+1)
# dp[1] = p_lst[1]
# for i in range(2, N+1):
#     dp[i] = max([dp[i-j]+p_lst[j] for j in range(1, i)]+[p_lst[i]])
#
# print(dp[N])