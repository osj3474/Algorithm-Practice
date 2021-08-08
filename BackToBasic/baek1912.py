# n = int(input())
# A = list(map(int, input().split()))
#
# MAX, sub_s = 0, 0
# flag = False
# for i in range(len(A)):
#     if A[i] > 0: flag = True
#     if sub_s+A[i] > 0:
#         sub_s += A[i]
#         if MAX < sub_s:
#             MAX = sub_s
#     else:
#         sub_s = 0
#
# if flag:
#     print(MAX)
# else:
#     print(max(A))

n = int(input())
lst = list(map(int, input().split()))

dp = [0]*n
dp[0]=lst[0]
for i in range(1, len(lst)):
    dp[i] = max(dp[i-1]+lst[i], lst[i])

print(max(dp))