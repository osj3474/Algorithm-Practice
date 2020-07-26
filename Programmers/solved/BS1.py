import math

def solution(b, M):
    b.sort(reverse = True)
    e = sum(b) - M 
    answer = 0
    if e <= 0:
        answer = max(b)
    else:
        i = 0
        for i in range(len(b)-1):
            if b[i] - b[i+1] >= e/(i+1):
                answer = b[i] - math.ceil(e/(i+1))
                break
            else:
                e = e - (b[i]-b[i+1])*(i+1)
        if i == len(b)-2:
            answer = math.floor(M/len(b))
    return answer
