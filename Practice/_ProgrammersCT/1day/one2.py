def solution(n):
    if n == 1:
        return [1]
    start = 0
    end = n-1
    cnt = 1
    lst = [[0]*(i+1) for i in range(n)]
    idx = 0
    while 1:
        for i in range(start, end+1):
            lst[i][idx]=cnt
            cnt += 1
        while idx < end:
            if lst[i].count(0) == 0:
                break
            idx += 1
            lst[i][idx]=cnt
            cnt += 1
        idx -=1
        i -= 1
        for i in range(i, start, -1):
            if lst[i].count(0) == 0:
                break
            lst[i][idx]=cnt
            idx -= 1
            cnt += 1
        idx += 1
        start += 2
        if start > end:
            break
        end -= 1
    answer_lst = list()
    for l in lst:
        answer_lst+=l
    return answer_lst

def main():
    n = 6
    print(solution(n))

main()
