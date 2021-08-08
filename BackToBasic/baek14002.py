N = int(input())
A_lst = list(map(int, input().split()))

dp = [[1,i] for i in range(N)]
MAX = 0
MAX_idx = 0

for i in range(N):
    temp = 0
    flag = False
    idx = i
    for j in range(i):
        if A_lst[i] > A_lst[j] and temp < dp[j][0]:
            temp = dp[j][0]
            idx = j
            flag = True
    if flag: dp[i] = [temp+1, idx]
    if MAX < dp[i][0]:
        MAX = dp[i][0]
        MAX_idx = i

value = 0
visited_lst = []
idx = MAX_idx
while value != 1:
    visited_lst.append(A_lst[idx])
    value, idx = dp[idx]

visited_lst.reverse()
print(MAX)
for visit in visited_lst:
    print(visit, end=' ')
