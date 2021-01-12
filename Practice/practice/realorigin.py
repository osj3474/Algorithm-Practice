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
        taken, val = fast_max(items, 40)
        for item in taken :
            print(item)
        print("Total value of items taken =", val)

def fast_max(sub_lst, avail, memo={}) :
    if (len(sub_lst), avail) in memo :
        return memo[(len(sub_lst), avail)]
    if sub_lst == [] or avail == 0 :
        return (), 0
    nextitem = sub_lst[0]
    if nextitem[2] <= avail : 
        chosen1, val1 = fast_max(sub_lst[1:], avail-nextitem[2], memo)
        val1 += nextitem[1]
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

main()
                     
