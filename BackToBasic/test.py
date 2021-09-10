N = int(input())
num_lst = list(map(int, input().split()))

isValid = False
for i in range(num_lst[0]+1, N+2):
    for j in range(N-1, 1, -1):
        if num_lst[j-1] < num_lst[j]:
            num_lst[j-1], num_lst[j] = num_lst[j], num_lst[j-1]
            isValid = True
            break
    if isValid: break
    num_lst = [i]+[k for k in range(1, N+1) if k!=i]
    isValid = True
    break


if isValid and len(num_lst)==N:
    for n in num_lst:
        print(n, end=' ')
else:
    print(-1)