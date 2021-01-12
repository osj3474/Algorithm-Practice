import random
def create_items(nitems, vmax, wmax) :
    items = []
    for i in range(nitems) :
        items.append((str(i+1), random.randint(1, vmax), random.randint(1, wmax)))
    return items


def main() :
    while True :
        no_items = input("Enter # of items: ")
        if no_items == "quit" :
            break
        no_items = int(no_items)
        items = create_items(no_items, 10, 10)
        items = [('1', 3, 5), ('2', 5, 2), ('3', 10, 10), ('4', 3, 2), ('5', 4, 3), ('6', 1, 1), ('7', 3, 10)]
        print(items)
        taken, val = fast_max(items, 20, tab=-1)
        for item in taken :
            print(item)
        print("Total value of items taken =", val)

# memo = { (남은 아이템 갯수, 남은 가방 용량) : (선택한 아이템들, 가치)}
# fast_max 리턴 값 = (선택한 아이템들, 가치)
def fast_max(sub_lst, avail, memo={}, tab=-1) :
    tab += 1
    # 특정 남은 용량에 대해 남은 아이템 갯수로 계산한 적이 있다면 (그때 선택한 아이템들, 가치) 리턴
    if (len(sub_lst), avail) in memo :
        print("{}# 남은 아이템 갯수가 ({})개이고, 남은 가방 용량이 ({})인 경우는 확인해서, ".format('\t'*tab, len(sub_lst), avail))
        print("{}# 바로 ({}) 리턴".format('\t'*tab, memo[(len(sub_lst), avail)]))
        return memo[(len(sub_lst), avail)]
    # 아이템이 없거나 용량이 없는 경우
    if sub_lst == [] or avail == 0 :  # 선택할 아이템이 없는 경우 or 남은 용량이 없는 경우
        print("{}# 선택할 아이템이 없는 경우 or 남은 용량이 없는 경우".format('\t'*tab))
        print("{}{} 리턴".format('\t'*tab,((), 0)))
        return (), 0
    nextitem = sub_lst[0]
    print("{}nextitem:".format('\t'*tab), nextitem)
    print("{}avail:".format('\t'*tab), avail)
    print("{}memo:".format('\t'*tab), memo)
    if nextitem[2] <= avail :
        print("{}재귀갑니다.1".format("\t" * tab))
        chosen1, val1 = fast_max(sub_lst[1:], avail-nextitem[2], memo, tab)
        print("{}[ Before ]".format('\t'*tab))
        print("{}val1:".format('\t'*tab), val1)
        print("{}chosen1:".format('\t'*tab), chosen1)
        print("{}(nextitem,):".format('\t'*tab), (nextitem,))
        val1 += nextitem[1]
        # chosen1, chosen2는 남은 용량에 들어갈 아이템의 후보이다.
        # chosen1은
        chosen1 = chosen1 + (nextitem,)
        print("{}[ After ]".format('\t'*tab))
        print("{}val1:".format('\t'*tab), val1)
        print("{}chosen1:".format('\t'*tab), chosen1)
        print("{}sub_lst[1:], avail, memo : ".format('\t'*tab), sub_lst[1:], avail, memo)
        print("")
        print("{}재귀갑니다.2".format("\t"*tab))
        chosen2, val2 = fast_max(sub_lst[1:], avail, memo, tab)
        print("{}val2:".format('\t'*tab), val2)
        print("{}chosen2:".format('\t'*tab), chosen2)

        if val1 > val2 :
            result = chosen1, val1
        else :
            result = chosen2, val2
    else :
        print("{}# 용량초과시 오는 곳".format('\t'*tab))
        print("{}# 내가 현재 들고 있는 아이템은 ({}) 이고,".format('\t'*tab, sub_lst[0]))
        print("{}# 남은 아이템들, ({})로 다시 재귀".format('\t'*tab, sub_lst[1:]))
        print("")
        print("{}재귀갑니다.3".format("\t" * tab))
        result = fast_max(sub_lst[1:], avail, memo, tab)
    print("{}memo ({}) 키에 ({}) 값 넣기".format('\t'*tab,(len(sub_lst), avail), result))
    memo[(len(sub_lst), avail)] = result
    print("{}memo:".format('\t'*tab), memo)
    return result

main()