n = int(input())
A = list(map(int, input().split()))

MAX = temp = A[0]
out = None
flag = True
cnt = 0
for i in range(1, len(A)):
    if A[i]<0:
        cnt += 1
        if out:
            if flag:
                temp += A[out]
            else:
                temp = sum(A[out+1:i])
        else:
            if temp+A[i]<0:
                flag =False
        out = i
        continue
    if temp+A[i] < 0:
        temp = 0
        continue
    temp += A[i]
    MAX = max(MAX, temp)

if cnt == len(A):
    print(min(A))
else:
    print(MAX)