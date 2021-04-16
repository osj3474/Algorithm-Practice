# sort, max, min 함수 쓰지 않고 풀기
N = int(input())
num_lst = list(map(int, input().split()))
# 아무리 quick sort라도 nlogn이니까, for문 한번 돌려서 n이 낫다
MAX = -float('inf')
MIN = float('inf')
for i in range(N):
    if MAX < num_lst[i]:
        MAX = num_lst[i]
    if MIN > num_lst[i]:
        MIN = num_lst[i]
print(MIN, MAX)


# sort, max, min 함수 사용
# num_lst.sort()
# print(num_lst[0], num_lst[-1])
# print(min(num_lst), max(num_lst))