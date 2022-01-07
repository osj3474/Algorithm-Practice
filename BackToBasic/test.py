# from itertools import combinations_with_replacement as cr
#
# N = int(input())
# words = [1, 5, 10, 50]
# ck = [False] * (50*N+1)
#
# case_lst = cr(words, N)
# for case in case_lst:
#     ck[sum(case)] = True
#
# print(ck.count(True))

# https://jinho-study.tistory.com/1039 이렇게 푸는게 맞는듯.