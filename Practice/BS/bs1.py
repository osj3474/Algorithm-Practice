def solution(n, times):
    length = len(times)
    MAX = n*max(times)
    minute_lst = [i for i in range(1, MAX+1)]
    low = 0
    high = len(minute_lst)
    while low<=high:
        mid = (low+high) // 2
        total, alpha = 0, 0
        for i in range(length):
            total += minute_lst[mid]//times[i]
            if minute_lst[mid] % times[i]:
                alpha += 1
        ck_lst = [i for i in range(total-alpha, total+1)]
        if n in ck_lst:
            break
        elif max(ck_lst) > n:
            high = mid-1
        elif min(ck_lst) < n:
            low = mid+1
    return minute_lst[mid]


def main():
    # n = 6
    # times = [4,10]  # 20
    n = 5
    times = [1,5,10]  # 5
    print(solution(n, times))

main()

