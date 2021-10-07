# 93%

def solution(N):
    MAX = 0
    cnt = 0
    flag = False

    q = N
    while True:
        q, r = divmod(q, 2)
        # print(q, r)
        if r==1:   # 한번만 들어올 수 있음.
            flag = True

        if flag:
            # 1을 만났음 이미
            if r==0:
                cnt+=1

            else:
                if MAX < cnt:
                    MAX = cnt
                cnt = 0

        if q == 1: break

    return MAX
