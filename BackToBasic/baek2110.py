# 입력 받기
n, k = map(int, input().split())
pole_lst = [int(input()) for _ in range(n)]
pole_lst.sort()


# 인자로 받은 공유기 간격을 기준으로 공유기를 설치해나간다.
def check(base):
    count = 1  # 맨 첫번째 전봇대는 바로 설치한다.
    now = 0
    fix = pole_lst[0]
    ##    print('fix:',fix)
    for i in range(n - 1):  # 전봇대 기준으로 반복문을 돌린다.
        m = pole_lst[i + 1] - fix
        if (m >= base):  # 최대 범위를 초과하면,
            ##            if(base == m):
            ##                now =1
            count += 1
            fix = pole_lst[i + 1]
    ##            print('fix:',fix)
    ##            if(fix != pole_lst[i+1]):
    ##                fix = pole_lst[i+1]
    ##                print('fix:',fix)
    ##            else:  # 바로 다음 전봇대라면, 간격을 줄여야 한다.
    ##                break
    ##    if(now == 0):
    ##        count+=1
    ##    print('count:',count)
    return count


if k == 2:
    print(pole_lst[-1] - pole_lst[0])

elif n == k:
    ret = 1000000000000000
    for i in range(len(pole_lst) - 1):
        dist = pole_lst[i + 1] - pole_lst[i]
        if ret > dist:
            ret = dist
    print(ret)

else:
    t = (pole_lst[-1] - pole_lst[0]) // (k - 1)

    ##    print('t:',t)

    low = 1
    high = t

    ret = 0

    while (low <= high):
        mid = (low + high) // 2
        ##        print('mid:',mid)
        # print('low:',low, 'high:',high)
        if check(mid) < k:
            high = mid - 1
        else:
            ret = max(ret, mid)
            low = mid + 1

    print(ret)
