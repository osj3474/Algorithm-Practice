numbers = [1,1,1,1,1]
target = 3

def find(lst, target):
    if not lst:
        if target==0:
            return 1
        else:
            return 0
    return find(lst[1:], target-lst[0])

def main(numbers, target):
    print(find(numbers, target))

main(numbers, target)