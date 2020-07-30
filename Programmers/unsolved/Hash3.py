def toDict(clothes):
    ret = {}
    for cloth in clothes:
        try:
            ret[cloth[1]] += 1
        except:
            ret.update({cloth[1]:1})
    return ret

from itertools import combinations as cb

def subset(dic):
    ret = [0] * len(dic)
    for i in range(1, len(dic)+1):
        ret[i-1] = list(cb(dic, i))
    return ret

def mulSum(clothes_dict, combination_subset_lst):
    cnt = 1
    ret = 0
    for combination_lst in combination_subset_lst:
        for combination in combination_lst:
            sub_total = 1
            for i in range(cnt):
                sub_total *= clothes_dict[combination[i]]
            ret += sub_total
        cnt += 1
    return ret

def solution(clothes):
    clothes_dict = toDict(clothes)
    combination_subset_lst = subset(clothes_dict)
    answer = mulSum(clothes_dict, combination_subset_lst)
    return answer
