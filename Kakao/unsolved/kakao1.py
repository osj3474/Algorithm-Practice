# 2, 7, 17, 18, 20, 21, 23, 27

import math

def splitWord(word, length, unit):
    ret = [0] * math.ceil(length/unit)
    i = 0
    for start in range(0, length, unit):
        end = start + unit
        if end >= length:
            ret[i] = word[start:]
        else:
            ret[i] = word[start:end]
        i += 1
    return ret

def makeNew(word_lst, length, unit):
    cnt = length   # 원래 전체 길이
    flag = 1       # flag는 word 앞에 숫자를 넣어야 하는지
    for i in range(len(word_lst)-1):      # 나눠진 word를 하나씩 접근
        if word_lst[i] == word_lst[i+1]:  # 앞, 뒤 word가 같으면
            cnt -= unit   # unit 만큼 빼고
            if flag:
                cnt += 1  # 같은 걸 처음 만난 거라면, word앞에 숫자가 더해짐
            flag = 0
        else:
            flag = 1
    return cnt

def solution(s):
    length = len(s)
    if length == 1:
        return 1
    limit = len(s)//2
    MIN = 100000
    for i in range(1, limit+1):
        word_lst = splitWord(s, length, i)
        cnt = makeNew(word_lst, length, i)
        MIN = min(MIN, cnt)
    return MIN

def main():
    s = "ababac"
    print(solution(s))

if __name__ == '__main__':
    main()


