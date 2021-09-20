def go(idx, answer:list, pocket):
    if len(answer) == 6:  # 조합을 구한 경우
        for a in answer:
            print(a, end=' ')
        print()
        return
    if idx==len(pocket): return     # 가진 수가 없는 경우
    go(idx+1, answer+[pocket[idx]], pocket)  # 해당 수를 선택하는 경우
    go(idx+1, answer, pocket)                # 해당 수를 선택하지 않는 경우


while True:
    k, *a = map(int, input().split())
    if k==0: break

    go(0, [], a)
    print()