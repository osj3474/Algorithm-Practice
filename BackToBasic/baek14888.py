# # 14888 PyPy3

N = int(input())
elements = list(map(int, input().split()))
oper_cnt_lst = list(map(int, input().split()))
from itertools import permutations as pm

def cnt2raw(cnt_lst):
    ret = list()
    for i, v in enumerate(cnt_lst):
        ret.extend(list([i]*v))
    return ret

def operation(n1, n2, oper):
    ret = 0
    if oper==0: ret=n1+n2
    elif oper==1: ret=n1-n2
    elif oper==2: ret=n1*n2
    else:
        if n2==0: return '-1'
        if n1<0:
            ret = (n1*(-1)//n2)*(-1)
        else: ret = n1//n2
    return ret

oper_raw_lst = cnt2raw(oper_cnt_lst)
oper_case = list(pm(oper_raw_lst, N-1))

MAX=float('-inf')
MIN=float('inf')

for oper_lst in oper_case:
    value = operation(elements[0], elements[1], oper_lst[0])
    for i in range(2, N):
        value = operation(value, elements[i], oper_lst[i-1])
        if value == '-1': break
    if value != '-1':
        if MAX < value: MAX = value
        if MIN > value: MIN = value

print(MAX)
print(MIN)



