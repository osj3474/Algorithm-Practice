def fast_max(sub_lst, avail, memo={}) :
    # 특정 남은 용량에 대해 남은 아이템 갯수로 계산한 적이 있다면 (그때 선택한 아이템들, 가치) 리턴
    if (len(sub_lst), avail) in memo :
        return memo[(len(sub_lst), avail)]
    # 아이템이 없거나 용량이 없는 경우
    if sub_lst == [] or avail == 0 :  # 선택할 아이템이 없는 경우 or 남은 용량이 없는 경우
        return (), 0
    nextitem = sub_lst[0]
    if nextitem[0] <= avail :
        chosen1, val1 = fast_max(sub_lst[1:], avail-nextitem[0], memo)
        val1 += nextitem[1]
        # chosen1, chosen2는 남은 용량에 들어갈 아이템의 후보이다.
        # chosen1은
        chosen1 = chosen1 + (nextitem,)
        chosen2, val2 = fast_max(sub_lst[1:], avail, memo)

        if val1 > val2 :
            result = chosen1, val1
        else :
            result = chosen2, val2
    else :
        result = fast_max(sub_lst[1:], avail, memo)
    memo[(len(sub_lst), avail)] = result
    return result

def solution():
    N, K = map(int, input().split())
    item_lst = [list(map(int, input().split())) for _ in range(N)]
    result_lst, answer = fast_max(item_lst, K)
    print(answer)


solution()