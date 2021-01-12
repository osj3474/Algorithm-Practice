from itertools import combinations as cb

def solution(distance, rocks, n):
    idx_lst = list(range(len(rocks)))
    combi_lst = list(map(list, list(cb(idx_lst, len(rocks)-n))))
    rocks.sort()
    length = len(rocks)
    MAX = 0
    for combi in combi_lst:
        now = list(map(rocks.__getitem__, combi))
        now.extend([distance])
        MIN = now[0]
        for i in range(length-n):
            gap = now[i+1]-now[i]
            if MIN > gap:
                MIN = gap
        if MAX < MIN:
            MAX = MIN
    return MAX

def main():
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2
    print(solution(distance, rocks, n))

main()


