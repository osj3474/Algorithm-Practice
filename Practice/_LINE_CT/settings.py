from collections import defaultdict
a = defaultdict(list)

import re
p = re.compile('[a-z]+|[0-9]+')
p = re.compile(r'([\w|-]+) and ([\w|-]+) and ([\w|-]+) and ([\w|-]+) (\d+)')
p.findall("text")

def makeLongArray(multi_lst, N):
    long_lst = list()
    for lst in multi_lst:
        long_lst += lst
    return long_lst

def makeMultiArray(one_lst, N):
    ret = []
    for i in range(0,N**2,N):
        ret.append(one_lst[i:i+N])
    return ret

def rotate(lst, N, idx_lst):
    i = 0
    new_lst = [0]*N**2
    for idx in idx_lst:
        new_lst[i] = lst[idx]
        i += 1
    return new_lst

