def solution(p_lst):
    length = len(p_lst)
    int_lst = sorted(list(map(int, p_lst)))
    p_lst = list(map(str, int_lst))
    for i in range(length-1):
        digit_len = len(p_lst[i])
        for j in range(i+1, length):
            if p_lst[i] in p_lst[j][:digit_len]:
                return False
    return True
