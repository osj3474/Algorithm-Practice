def solution(citations):
    citations.sort()
    length = len(citations)
    ck = [i for i in range(length,0,-1)]
    answer_lst = list()
    for i in range(length):
        if citations[i] >= ck[i]:
            answer_lst.append(ck[i])
    try:
        answer = max(answer_lst)
    except:
        answer = 0
    return answer