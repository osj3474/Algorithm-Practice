n = int(input())
A = list(map(int, input().split()))

MAX, sub_s = 0, 0
flag = False
for i in range(len(A)):
    if A[i] > 0: flag = True
    if sub_s+A[i] > 0:
        sub_s += A[i]
        if MAX < sub_s:
            MAX = sub_s
    else:
        sub_s = 0

if flag:
    print(MAX)
else:
    print(max(A))