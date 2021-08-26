from collections import Counter
from math import ceil
cnt_dic = Counter(input())
six_nine = 0
last = 0

for k, v in cnt_dic.items():
    if k=='6' or k=='9': six_nine += v
    else:
        if last<v: last = v

print(max(last, ceil(six_nine/2)))