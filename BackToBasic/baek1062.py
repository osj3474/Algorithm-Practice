N, K = map(int, input().split())
word_lst = [input() for _ in range(N)]

from itertools import combinations as cb

def solution(N, K, word_lst):
    if K < 5: return 0
    if K==26: return N

    MAX = 0
    alpa_set = set()
    word_seperated_lst = [set() for _ in range(N)]
    for i in range(len(word_lst)):
        word = word_lst[i][4:-4]
        for w in word:
            if w not in (['a', 'c', 'i', 'n', 't']):
                word_seperated_lst[i].add(w)
            alpa_set.add(w)

    alpa_lst = []
    for i in range(97, 123):
        alpa = chr(i)
        if alpa in alpa_set and alpa not in (['a', 'c', 'i', 'n', 't']):
            alpa_lst.append(alpa)

    case_lst = list(cb(alpa_lst, K-5))
    if not case_lst:
        return N

    for case in case_lst:
        cnt = 0
        for word in word_seperated_lst:
            flag = True
            for w in word:
                if w not in case: flag = False; break
            if flag: cnt += 1
        if MAX < cnt:
            MAX = cnt
    return MAX

print(solution(N, K, word_lst))