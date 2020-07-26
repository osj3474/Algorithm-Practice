def solution(h):
    length = len(h)
    answer = [0] * length
    for i in range(length-1, 0, -1):
        for j in range(i, 0, -1):
            if h[i] < h[j-1]:
                answer[i] = j
                break
    return answer
