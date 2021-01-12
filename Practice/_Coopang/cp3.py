from collections import defaultdict

def solution(k, score):
    length = len(score)
    diff_dic = defaultdict(int)   # key:거리, value:횟수
    diff_lst = [0]*length
    MAX = set()

    idx_lst = [i for i in range(length)]
    idx_set = set(idx_lst)

    for i in range(1, length):
        diff_lst[i] = score[i-1]-score[i]
        now_diff = diff_lst[i]

        diff_dic[now_diff]+=1
        if k<=diff_dic[now_diff]:
            MAX.add(now_diff)
    diff_dic = dict(diff_dic)

    for i in range(1, length):
        for ma in MAX:
            if ma == diff_lst[i]:
                try:
                    idx_set.remove(i)
                    idx_set.remove(i-1)
                except:
                    pass
    answer = len(idx_set)
    return answer

def main():
    k = 3
    score = [24,22,20,10,5,3,2,1]
    print(solution(k, score))

main()

