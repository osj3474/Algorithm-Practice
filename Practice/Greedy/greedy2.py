def selectNum(number_int, k):
    pickedNum = 0
    length = len(number_int)
    for i in range(9, -1, -1):
        try:
            for j in range(length):
                if number_int[j] == i:
                    idx = j
                    break
            if idx <= k:
                pickedNum = number_int[idx]
                number_int = number_int[idx+1:]
                k -= idx
                break
        except:
            pass
    return pickedNum, number_int, k

def solution(number, k):
    number_int = list(map(int, number))
    num_lst = [0] * (len(number)-k)
    print("here?", num_lst[100])
    i = 0
    while k>0:
        print(i)
        num, number_int, k = selectNum(number_int, k)
        num_lst[i] = num
        i+=1
    num_lst = num_lst[:i]
    num_lst += number_int
    ret = ''
    for num in num_lst:
        ret += str(num)
    return ret

def main():
    number = "480325707673740"
    print(len(number))
    k = 50
    print(solution(number, k))

main()
