# 입력 받은 자릿수까지의 모든 소수를 구해서 그 리스트 안에서 입력받은 자릿수에
# 해당하는 수들만 검사를 하는 방법으로 진행했다.
# 검사는 첫번째 자릿수는 2,3,5,7 만 확인하면 되고, 마지막 자릿수가 소수인지는 이미
# 걸러진 상태이다. 그래서 그 첫번째 자릿수와 입력받은 자릿수의 두 수의 경우를 제외하고
# 검사를 진행한다. 검사는 N이 최대 8이라서 구했던 소수 리스트 안에 있는지 없는지로 해도 될 것이라
# 판단했다. 그런데 메모리 초과가 떳다.

N = int(input())

def era(N):
    ck = [False for _ in range(N+1)]
    ret = []
    for i in range(2, len(ck)):
        if ck[i]:
            continue
        ret.append(i)
        for j in range(i**2, len(ck), i):
            ck[j] = True
    return ret

target = 10**N
lst = era(target)
low = 0
high = len(lst)

target //= 10
while low <= high:
    mid = (low + high) // 2
    if lst[mid] == target:
        break
    elif lst[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

candidate_lst = lst[mid+1:]



def check(n):
    flag = 1
    n_str = str(n)
    for i in range(1, N):
        if int(n_str[:i]) not in lst:
            flag=0
    if flag==0:
        return 0
    return 1



answer_lst = []
for candidate in candidate_lst:
    if check(candidate):
        answer_lst.append(candidate)

print(answer_lst)