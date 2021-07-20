# from collections import Counter
#
# N, K = map(int, input().split())
# use_lst = list(map(int, input().split()))
#
# count_dic = Counter(use_lst)
# cnt = 0
# pocket_lst = list()
# pocket_set = set()
#
# limit = 0
# for ele in use_lst:
#     if ele in pocket_set:
#         print("{}넣으려고 했는데 있네.".format(ele))
#         continue
#     if limit >= N:
#         pocket_lst = sorted(pocket_lst, key=lambda x:-x[1])
#
#         temp= pocket_lst.pop()
#         pocket_set.remove(temp[0])
#         print("{}넣으려고 {} 빠져나갑니다.".format(ele,temp))
#         cnt += 1
#         limit -= 1
#         print("cnt={}".format(cnt))
#     count_dic[ele] -= 1
#     pocket_lst.append([ele, count_dic[ele]])
#     pocket_set.add(ele)
#     limit+=1
#     # print(pocket_lst, limit, cnt)
#     print(pocket_lst)
#
# print(cnt)
#
#
# a = [[1,3], [2, 2], [3, 1]]
# a=sorted(a, key=lambda x:-x[1])
# print(a)
#
#

from collections import Counter

N, K = map(int, input().split())
use_lst = list(map(int, input().split()))

count_dic = Counter(use_lst)
cnt = 0
pocket_lst = list()
pocket_set = set()

limit = 0
for ele in use_lst:
    if ele in pocket_set: continue
    if limit >= N:
        # pocket_lst = sorted(pocket_lst, key=lambda x:-x[1])
        # temp= pocket_lst.pop()
        flag = True
        for pocket in pocket_lst:
            if count_dic[pocket[0]]==0:
                pocket_lst.remove(pocket)
                pocket_set.remove(pocket)
                flag = False
                break
        if flag:
            for i in range(N-1, 0, -1):
                if use_lst[i] in pocket_set:
                    pocket_lst.remove(use_lst[i])
                    pocket_set.remove(pocket_lst[i])
                    break
        cnt += 1
        limit -= 1
    count_dic[ele] -= 1
    pocket_lst.append([ele, count_dic[ele]])
    pocket_set.add(ele)
    limit+=1

print(cnt)



