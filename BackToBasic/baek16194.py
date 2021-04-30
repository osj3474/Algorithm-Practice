N = int(input())
card_lst = [0]+list(map(int, input().split()))


# D[n] = N개를 갖기위해 지불해야하는 금액의 최댓값

memo = [0]*(N+1)
for i in range(1, N+1):
    for j in range(1, i+1):
        memo[i] = min(memo[i], memo[i-j]+card_lst[j])

print(memo[N])