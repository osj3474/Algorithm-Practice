def solution(origin_lst):
    length = len(origin_lst)
    cnt = 0
    for target in origin_lst:
        # print(origin_lst)
        # print("난 지금 이걸 볼거야 :", target)
        a_lst = origin_lst[:]
        i, j, term, ret = 0, 1, 0, set()
        while j < length:
            # print("a_lst[i], a_lst[j] :", a_lst[i], a_lst[j])
            if a_lst[i] < a_lst[j]:   # 오른쪽이 더 커
                larger = a_lst[j]
                if larger != target:
                    term += 1
                    j += 1
                else:
                    ret.add(a_lst[i])
                    ret.add(a_lst[j])
                    i += 1
                    j += 1
            else:    # 왼쪽이 더 커
                larger = a_lst[i]
                # if larger == target:
                ret.add(a_lst[i])
                i += term+1
                j += 1
                term = 0
            # print(ret)
        print(ret)
        if len(ret) <= 2:
            cnt += 1
    return cnt

def main():
    a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
    print(solution(a))

main()
