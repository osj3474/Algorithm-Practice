# from collections import Counter
from itertools import combinations as cb

def solution(orders, course):
    answer_lst = list()
    for n in course:
        combi_dic = dict()
        for order in orders:
            combi_lst = list(cb(list(order), n))   # nCr : cb(n, r)
            # ["XY", "XZ", "YZ"]
            for combi in combi_lst:
                combi = sorted(list(combi))
                try:
                    combi_dic[str(set(combi))] += 1
                except:
                    combi_dic[str(set(combi))] = 1
        try:
            MAX = max(combi_dic.values())
        except:
            MAX = 0
        print(combi_dic)
        if MAX >= 2:
            for i, v in combi_dic.items():
                if MAX == v:
                    lst = list()
                    for c in i:
                        asc = ord(c)
                        if asc>=65 and asc<=90:
                            lst.append(chr(asc))
                    lst.sort()
                    answer_lst.append(''.join(lst))
    answer_lst.sort()
    return answer_lst

def main():
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]
    print(solution(orders, course))

main()
#
# # a= ['a', 'v']
# # b = ['v','a']
# # if set(a) == set(b):
# #     print(1)

# a = {'E', 'D', 'A'}
# a = ''.join(sorted(list(a)))
# print(a)