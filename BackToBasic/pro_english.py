def solution(n, words):
    answer = [0, 0]
    past_lst = set([words[0]])
    mod = [n] + [i for i in range(1, n)]
    length = len(words)

    for i in range(length - 1):
        if words[i][-1] != words[i + 1][0]: break
        if words[i + 1] in past_lst: break
        if len(words[i + 1]) < 2: break
        past_lst.add(words[i + 1])

    if len(past_lst) != length:
        answer = [mod[(i + 2) % n], (i + 1) // n + 1]

    return answer