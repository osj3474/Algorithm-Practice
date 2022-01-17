X, Y = map(int, input().split())
Z = Y*100//X

answer = -1
if Z>=99: pass
else:
    low, high = 0, 1000000000

    while(low <= high):
        mid = (low + high)//2
        newZ = (Y+mid)*100//(X+mid)

        if newZ > Z:  # newZ==target 인 경우에도 증가가 필요
            high = mid-1
        else:
            low = mid+1
    answer = low

print(answer)