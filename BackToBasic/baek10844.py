# 각 자리수에 올 수 있는 수는 0~9 이다. (첫번째 수는 0 제외)
# 각 자리에 대한 10개의 배열을 가진다.
# 가령, N=4인 경우를 생각해보자.
# 만약 일의 자리 수를 3인 경우를 찾아본다면,
# 3의 앞자리는 2와 4가 올 수 있다.
# 2의 앞자리는 1과 3이, 4의 앞자리는 3과 5가 올 수 있다.
# 1의 앞자리는 2가 올 수 있고, ......
# 이렇게 가능한 일의 자리수만큼의 배열을 가지고,
# 값으로는 가능한 경우의 수를 가진다.
# 다시말해 d[0~9]가 있고, 정답은 sum(d[n])이 된다는 것.
# 하지만, 현재 dp문제이고, 분명 시간복잡도로 모든 문제는 한번만 풀어야 할 것이다.
# 따라서, 입력값인 N만큼의 배열을 0~9만큼의 크기로 가질 것이다.
# ex) 4자리 수 =
# [[0~9], [0~9], [0~9], [0~9]] 를 하자는 것이다.
# 물론, 0으로 시작하는 수는 없기 때문에, 첫번째 인덱스의 0의 값은 0이 될 것이다.
# 만들 수 있는 모든 조합의 수는 9*10*10*10 이겠지만,
# 여기서 안 되는 것들이 있다. 최종적인 답은 sum(D[N])으로 구한다.
# d[i][j] = 길이가 i인 계단수의 갯수(마지막 수 : j)
#         = d[i-1][j-1] + d[i-1][j+1]
# 단, 0보다 1작은수, 9보다 1큰수는 제외해야한다.

# 일단 첫째자리에 0이 올 수 있다고 가정하고 dp값을 채운다.
# dp[i][j] = i자리 계단수 (이전 수 = j)  // 앞에서부터 채워 감
# dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1] // (0과 9만 다름)
# 마지막에 0으로 시작하는 dp[n][0] 만 빼주면 됨.

N = int(input())

def solution(N):
    if N==1: return 9
    dp = [[0]*10 for _ in range(N+1)]

    for i in range(10):
        dp[1][i]=1

    for i in range(2, N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1, 9):
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])%1000000000
    return (sum(dp[N])-dp[N][0])%1000000000

print(solution(N))











print(answer % mod)