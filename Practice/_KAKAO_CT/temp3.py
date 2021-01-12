target = 200
lst = [150, 210, 150, 260, 80, 50]

low = 0
high = len(lst)

lst.sort()
print(lst)
while low <= high:
    mid = (low + high) // 2
    if lst[mid] == target:
        break
    elif lst[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

idx = 0
if lst[mid] < target:
    idx = mid
else:
    idx = mid - 1
print(idx)
print(lst[idx+1:])