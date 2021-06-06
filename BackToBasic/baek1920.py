N = int(input())
N_set = set(list(map(int, input().split())))
M = int(input())
M_lst = list(map(int, input().split()))

for m in M_lst:
    if m in N_set: print(1)
    else: print(0)
