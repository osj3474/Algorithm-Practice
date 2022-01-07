from itertools import combinations_with_replacement as cr

N = int(input())
words = [1, 5, 10, 50]
ck = [False] * (50*N+1)

case_lst = cr(words, N)
for case in case_lst:
    ck[sum(case)] = True

print(ck.count(True))

# https://jinho-study.tistory.com/1039 이렇게 푸는게 맞는듯.
# N = int(input())
# s = set()
# for i in range(N+1):
#     for j in range(N+1 - i):
#         for k in range(N+1 - i - j):
#             t = N-i-j-k
#             n = i + 5*j + 10*k  + 50*t
#             s.add(n)
#
# print(len(s))