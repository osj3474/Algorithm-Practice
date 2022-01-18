# A, B 각각에 대하여 부분합을 먼저 구해서 경우를 찾는 것은 맞는데,
# 맹점은 거기가 아니라 A, B 부분합을 2중 for문을 돌리면 안된다는 것에 있다.
# 그래서 A, B 모두 defaultdict을 쓰면 아래처럼 간단하게 풀 수 있는데
# for a in A_sub.keys():
#     answer += A_sub[a] * B_sub[T-a]
# 메모리 초과가 나서
# B 하나만 dictionary를 써서 2중 for문을 1중 for문으로 줄인다.

from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sub = []
for i in range(n):
    for j in range(i, n):
        temp = sum(A[i:j+1])
        A_sub.append(temp)


B_sub = defaultdict(int)  # 2중 for문 없애야 함 ==> 메모리 초과 때문에 ==> dictionary 하나만 쓰기
for i in range(m):
    for j in range(i, m):
        temp = sum(B[i:j+1])
        B_sub[temp] += 1

answer = 0
for a in A_sub:
    answer += B_sub[T-a]


print(answer)