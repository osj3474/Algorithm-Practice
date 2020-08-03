import math

def solution(pro, sp):
    length = len(pro)
    if length == 1:
        return [1]
    completeDay = [0] * length
    deployDay = []
    for i in range(length):
        completeDay[i] = math.ceil((100-pro[i])/sp[i])
    cnt = 1
    idx = 0
    for i in range(length-1):
        if completeDay[idx] < completeDay[i+1]:
            deployDay.append(cnt)
            cnt = 1
            idx = i+1
            continue
        cnt += 1
    deployDay.append(cnt)
    return deployDay


