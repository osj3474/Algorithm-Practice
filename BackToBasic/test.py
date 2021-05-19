N_str = input()
M = int(input())
A_set = set(map(int, input().split()))
A_lst = list(set([i for i in range(10)]) - A_set)
A_lst.sort()

def find_nearest(n):
    MIN = 10
    ret = 0
    for i in range(len(A_lst)):
        temp = abs(A_lst[i]-n)
        if MIN > temp:
            MIN = temp
            ret = A_lst[i]
    return ret

s_idx = 0
num = ''

if A_lst[0]==0:
    MIN = 10
    ret = 0
    k = int(N_str[0])
    for i in range(1, len(A_lst)):
        temp = abs(A_lst[i]-k)
        if MIN > temp:
            MIN = temp
            ret = A_lst[i]
    num += str(ret)
    s_idx = 1

for i in range(s_idx, len(N_str)):
    num += str(find_nearest(int(N_str[i])))

answer = len(N_str)+abs(int(N_str)-int(num))
print(min(answer, abs(100-int(N_str))))