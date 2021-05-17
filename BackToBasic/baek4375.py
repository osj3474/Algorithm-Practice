# 처음에 문제를 잘 이해를 못했는데,
# 입력 갯수는 안 말해주고, 한 줄당 그에 대한 출력을 해야함.
# 입력받은 수를
# 1, 11, 111, 1111, .... 로 나눌때, 나머지가 0이 되는 수의 자릿수를 구하는 문제

while True:
    try: n = int(input())
    except: break
    div, idx, ten = 1, 1, 1
    while True:
        q = div % n
        if q==0:
            print(idx)
            break
        ten = ten*10
        div += ten
        idx += 1
