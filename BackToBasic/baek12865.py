N, K = map(int, input().split())
w, v = [0]*N, [0]*N
for i in range(N):
    w[i], v[i] = map(int, input().split())

# dp[i][j] = i번째 까지의 물건 안에서, 캐파가 j만큼 남았을 때의 최대 가치
# 궁극적으로 원하는 건 = dp[N][K] 이다.
# 생각은 l, m을 본다고 했을 때, 이전에 어떤 물건을 샀는지는 생각도 하지 않고,
# 딱 그 순간 i번째 물건을 살지 안 살지만 결정하고,
# 산다면, i를 제외하기 위해 i-=1 하고, 캐파도 w[i] 만큼해야한다.
# 안산다 하더라도, i는 제외이고(i-=1), 캐파는 변동 없다.
# 만약, 애초에 i번째 물건이 나의 모든 캐파를 가지고도 못 사는 거였다면,
# 그냥 바로 윗칸 꺼(i번째 물건이 없다고 했을 때의 최대 가치이니까.)를 받자.

dp = [[0]*(K+1) for _ in range(N)]
for i in range(N):
    for j in range(1, K+1):
        # 기본적으로 캐파가 허락해줘야한다.
        if j>=w[i]:
            # 산다/안산다 는 더 높은 가치로 판단
            # 비교는 바로 윗칸이다. 왜냐하면,
            # 캐파가 늚으로써 물건 선택지가 바뀌었을 수도 있기 때문이다.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][K])