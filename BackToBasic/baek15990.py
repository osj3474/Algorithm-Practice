# D[n] = n을 1,2,3의 합으로 나타낼 수 있는 경우의 수
# (연속된 수 X)
# => 마지막 수를 i라 두자. {A-i}의 원소만 가능

# D[n][1] = D[n-1][2] + D[n-1][3]
# D[n][2] = D[n-2][1] + D[n-2][3]
# D[n][3] = D[n-3][1] + D[n-3][2]