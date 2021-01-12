def fast_max(sub_lst, avail) :
    if sub_lst == [] or avail == 0 :
        return (), 0
    nextitem = sub_lst[0]
    if nextitem[2] <= avail : 
        chosen1, val1 = fast_max(sub_lst[1:], avail-nextitem[2])
        val1 += nextitem[1]
        chosen1 = chosen1 + (nextitem,)
        chosen2, val2 = fast_max(sub_lst[1:], avail)
        if val1 > val2 :
            result = chosen1, val1
        else :
            result = chosen2, val2
    else :
        result = fast_max(sub_lst[1:], avail)
    return result

items = [('1', 3, 5), ('2', 5, 2), ('3', 10, 10), ('4', 3, 2), ('5', 4, 3), ('6', 1, 1), ('7', 3, 10)]
taken, val = fast_max(items, 20)
for item in taken :
    print(item)
print("Total value of items taken =", val)