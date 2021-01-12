def solution(n, times):
    MAX = max(times)*n//len(times)
    lst = [i for i in range(MAX)]  # 이 중에 정답이 있다.
    low, high = 0, len(lst)
    while low<=high:
        mid = (low+high) // 2
        pass_cnt = 0

        for time in times:
            pass_cnt += lst[mid]//time
            if pass_cnt > n:
                high = mid-1
                break
        if n == pass_cnt:
            break
        else:
            low = mid+1
    return mid

def main():
    n = 1
    times = [2,2]
    print(solution(n, times))

main()