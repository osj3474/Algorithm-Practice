# method 1
# result 28776KB, 72ms
N, K = map(int, input().split())
answer = 0
cnt = 0

for i in range(1, N+1):
    if N%i == 0:
        cnt += 1
        if K == cnt:
            answer = i
            break

print(answer)


# method 2
# result 28776KB, 64ms
# N, K = map(int, input().split())
# answer = 0
# common_lst = [1]
#
# for i in range(2, N+1):
#     if N%i == 0:
#         common_lst.append(i)
#
# if len(common_lst) >= K:
#     answer = common_lst[K-1]
#
# print(answer)