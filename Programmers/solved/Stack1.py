def solution(prices):
    length = len(prices)
    answer = [0] * length
    for i in range(length):
        cnt = 0
        for j in range(i+1, length):
            cnt+=1
            if prices[j] < prices[i]:
                break
        answer[i]=cnt
    return answer

