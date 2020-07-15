def solution(answers):
    # 반복 패턴
    first = [1, 2, 3, 4, 5]
    f_len = len(first)
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    s_len = len(second)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    t_len = len(third)
    # 각 사람 맞은 횟수
    corret_lst = [0] * 3
    for i in range(len(answers)):
        if answers[i] == first[(i%f_len)]:
            corret_lst[0] += 1
        if answers[i] == second[(i%s_len)]:
            corret_lst[1] += 1
        if answers[i] == third[(i%t_len)]:
            corret_lst[2] += 1
    ret = []
    for i in range(3):
        if max(corret_lst) == corret_lst[i]:
            ret.append(i+1)
    return ret
